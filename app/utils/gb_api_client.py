import httpx

class GoogleBooksAPIClient:
    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/volumes"

    async def search_books(self, query):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.base_url, params={"q": query})
            response.raise_for_status()
            return response.json()
