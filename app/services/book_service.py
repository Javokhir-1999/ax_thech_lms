from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.book import Book
from app.dto.book_dto import BookCreateDTO, BookUpdateDTO, BookOutDTO

async def create_book(db: AsyncSession, book_create_dto: BookCreateDTO) -> BookOutDTO:
    book = Book(**book_create_dto.dict())
    db.add(book)
    await db.commit()
    await db.refresh(book)
    return BookOutDTO.from_orm(book)

async def get_book_by_isbn(db: AsyncSession, isbn: str) -> BookOutDTO:
    result = db.execute(select(Book).where(Book.isbn == isbn))
    book = result.scalars().first()
    if book is None:
        return None
    return BookOutDTO.from_orm(book)

async def get_books(db: AsyncSession) -> list[BookOutDTO]:
    result = await db.execute(select(Book))
    books = result.scalars().all()
    return [BookOutDTO.from_orm(book) for book in books]

async def update_book(db: AsyncSession, book_id: int, book_update_dto: BookUpdateDTO) -> BookOutDTO:
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalars().first()
    if not book:
        return None
    update_data = book_update_dto.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(book, key, value) if value is not None else None
    await db.commit()
    await db.refresh(book)
    return BookOutDTO.from_orm(book)
