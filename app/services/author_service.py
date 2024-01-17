from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.author import Author
from app.dto.author_dto import AuthorCreateDTO, AuthorUpdateDTO, AuthorOutDTO

async def create_author(db: AsyncSession, author_create_dto: AuthorCreateDTO) -> AuthorOutDTO:
    author = Author(**author_create_dto.dict())
    db.add(author)
    await db.commit()
    await db.refresh(author)
    return AuthorOutDTO.from_orm(author)

async def get_authors(db: AsyncSession) -> list[AuthorOutDTO]:
    result = await db.execute(select(Author))
    authors = result.scalars().all()
    return [AuthorOutDTO.from_orm(author) for author in authors]

async def get_author_by_id(db: AsyncSession, author_id: int) -> AuthorOutDTO:
    result = await db.execute(select(Author).filter_by(id=author_id))
    author = result.scalars().first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return AuthorOutDTO.from_orm(author)

async def update_author(db: AsyncSession, author_id: int, author_update_dto: AuthorUpdateDTO) -> AuthorOutDTO:
    query = select(Author).filter_by(id=author_id)
    result = await db.execute(query)
    author = result.scalars().first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    for var, value in vars(author_update_dto).items():
        setattr(author, var, value) if value is not None else None

    db.add(author)
    await db.commit()
    await db.refresh(author)
    return AuthorOutDTO.from_orm(author)

async def delete_author(db: AsyncSession, author_id: int):
    query = select(Author).filter_by(id=author_id)
    result = await db.execute(query)
    author = result.scalars().first()
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    await db.delete(author)
    await db.commit()
