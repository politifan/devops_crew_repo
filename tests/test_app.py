from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_homepage_renders() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "DevOps Crew Training" in response.text
    assert "FastAPI training project" in response.text


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_api_info_contains_training_tasks() -> None:
    response = client.get("/api/info")

    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "DevOps Crew Training Site"
    assert "write GitHub Actions CI" in payload["tasks"]
