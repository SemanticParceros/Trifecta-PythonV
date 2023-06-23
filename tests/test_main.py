from fastapi.testclient import TestClient
from fastapi import status
from src.main import app

client=TestClient(app)

def test_index_returns_corrects():
    response = client.get("/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}




