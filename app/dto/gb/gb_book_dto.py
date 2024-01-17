from pydantic import BaseModel

class BookSearchQuery(BaseModel):
    query: str
