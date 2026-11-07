from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/healthz").json() == {"status": "ok"}


def test_mock_generation_contract() -> None:
    response = client.post(
        "/v1/generate",
        json={"provider": "mock", "prompt": "Explain hybrid retrieval."},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["provider"] == "mock"
    assert payload["model"] == "deterministic-mock-v1"
    assert payload["usage"]["input_tokens"] > 0
    assert payload["trace_id"].startswith("tr_")


def test_validation_rejects_empty_prompt() -> None:
    response = client.post("/v1/generate", json={"provider": "mock", "prompt": ""})
    assert response.status_code == 422

