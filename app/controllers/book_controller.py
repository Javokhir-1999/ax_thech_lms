from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.book_service import create_book, get_book_by_isbn, get_books, update_book
from app.dto.book_dto import BookCreateDTO, BookUpdateDTO, BookOutDTO

router = APIRouter()

@router.post("/", response_model=BookOutDTO)
async def create_book_endpoint(book_create_dto: BookCreateDTO, db: AsyncSession = Depends(get_db)):
    return await create_book(db, book_create_dto)

@router.get("/{isbn}", response_model=BookOutDTO)
async def get_book_by_isbn_endpoint(isbn: str, db: AsyncSession = Depends(get_db)):
    book = await get_book_by_isbn(db, isbn)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/", response_model=list[BookOutDTO])
async def get_books_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_books(db)

@router.put("/{book_id}", response_model=BookOutDTO)
async def update_book_endpoint(book_id: int, book_update_dto: BookUpdateDTO, db: AsyncSession = Depends(get_db)):
    updated_book = await update_book(db, book_id, book_update_dto)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book
