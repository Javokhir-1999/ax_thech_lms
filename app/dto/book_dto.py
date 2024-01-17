from pydantic import BaseModel
from typing import Optional
from datetime import date

class BookBaseDTO(BaseModel):
    title: str
    author_id: int
    language: str
    publication_date: date
    category: str
    isbn: str

class BookCreateDTO(BookBaseDTO):
    pass

class BookUpdateDTO(BaseModel):
    title: Optional[str] = None
    author_id: Optional[int] = None
    language: Optional[str] = None
    publication_date: Optional[date] = None
    category: Optional[str] = None
    isbn: Optional[str] = None

class BookOutDTO(BookBaseDTO):
    id: int

    class Config:
        from_attributes = True
