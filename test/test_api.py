from fastapi.testclient import TestClient

from app import fast_app


client = TestClient(fast_app)


def test_first_view():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message":"TeSt"}
