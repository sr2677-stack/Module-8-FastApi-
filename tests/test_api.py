from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_add_api():
    response = client.get("/add?a=2&b=3")
    assert response.json()["result"] == 5

def test_divide_api():
    response = client.get("/divide?a=10&b=2")
    assert response.json()["result"] == 5

def test_divide_by_zero_api():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400