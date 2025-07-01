from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from schemas.user_schemas import UserCreate, UserLogin, UserOut, Token, UserLogOut
from models.db_models import User, UserRole, UserLog
from core.security import get_password_hash, verify_password, create_access_token
from core.config import settings
from deps.deps import get_db, get_current_user, require_admin
from datetime import datetime, timedelta
from typing import List

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.login == user_in.login).first():
        raise HTTPException(status_code=400, detail="Логин уже занят")
    user = User(
        login=user_in.login,
        password_hash=get_password_hash(user_in.password),
        display_name=user_in.display_name,
        role=UserRole.user,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=Token)
def login(user_in: UserLogin, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.login == user_in.login).first()
    ip = request.client.host if request.client else None
    if not user:
        log = UserLog(user_id=None, action="failed_login", ip=ip)
        db.add(log)
        db.commit()
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    # Проверка блокировки
    if user.failed_login_attempts >= settings.MAX_LOGIN_ATTEMPTS:
        if (
            user.last_failed_login
            and (datetime.utcnow() - user.last_failed_login).total_seconds()
            < settings.LOGIN_BLOCK_TIME_MINUTES * 60
        ):
            raise HTTPException(
                status_code=403, detail="Слишком много попыток. Попробуйте позже."
            )
        else:
            user.failed_login_attempts = 0
            db.commit()
    if not verify_password(user_in.password, user.password_hash):
        user.failed_login_attempts += 1
        user.last_failed_login = datetime.utcnow()
        db.add(UserLog(user_id=user.id, action="failed_login", ip=ip))
        db.commit()
        raise HTTPException(status_code=400, detail="Неверный логин или пароль")
    # Успешный вход
    user.failed_login_attempts = 0
    user.last_failed_login = None
    db.add(UserLog(user_id=user.id, action="login", ip=ip))
    db.commit()
    token = create_access_token({"sub": str(user.id), "role": user.role.value})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
def logout(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
    request: Request = None,
):
    ip = request.client.host if request and request.client else None
    db.add(UserLog(user_id=current_user.id, action="logout", ip=ip))
    db.commit()
    return {"msg": "Выход выполнен"}


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/logs", response_model=List[UserLogOut])
def get_logs(db: Session = Depends(get_db), user: User = Depends(require_admin)):
    return db.query(UserLog).order_by(UserLog.timestamp.desc()).all()


@router.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@router.get("/stats", tags=["Stats"])
def stats(db: Session = Depends(get_db)):
    total = db.query(User).count()
    admins = db.query(User).filter(User.role == UserRole.admin).count()
    return {"users": total, "admins": admins}
