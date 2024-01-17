from fastapi import APIRouter, Query
from app.utils.gb_api_client import GoogleBooksAPIClient

router = APIRouter()
google_books_api = GoogleBooksAPIClient()

@router.get("/books")
async def search_books(query: str = Query(..., description="Search query for books")):
    data = await google_books_api.search_books(query)
    return data
