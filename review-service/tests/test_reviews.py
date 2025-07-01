from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_review_unauthorized():
    response = client.post("/models/1/reviews", json={"rating": 5, "comment": "Test"})
    assert response.status_code == 401
