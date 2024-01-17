from fastapi.testclient import TestClient
from main import app
from app.utils.gb_api_client import GoogleBooksAPIClient

client = TestClient(app)

def test_search_books():
    gb_api = GoogleBooksAPIClient()
    query = "Glass Castle"
    response = client.get(f"/books?query={query}")
    
    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0
    total_items = data[0].get("totalItems")
    if total_items is not None:
        assert total_items > 0


