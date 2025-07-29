# file: test_integration.py
from app import app

def test_ping_route():
    client = app.test_client()
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {"message": "pong"}
