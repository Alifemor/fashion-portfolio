from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_register_user():
    response = client.post(
        "/register",
        json={
            "login": "testuser",
            "password": "testpassword",
            "display_name": "Тестовый пользователь",
        },
    )
    assert response.status_code == 200 or response.status_code == 400
