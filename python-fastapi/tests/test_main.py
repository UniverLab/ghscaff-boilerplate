from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_ping() -> None:
    response = client.get("/api/ping")
    assert response.status_code == 200
    assert response.json()["message"] == "pong"
