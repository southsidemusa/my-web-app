from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_list_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
