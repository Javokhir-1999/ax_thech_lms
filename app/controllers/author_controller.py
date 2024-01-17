from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.author_service import create_author, get_authors, get_author_by_id, update_author, delete_author
from app.dto.author_dto import AuthorCreateDTO, AuthorUpdateDTO, AuthorOutDTO

router = APIRouter()

@router.post("/", response_model=AuthorOutDTO)
async def create_author_endpoint(author_create_dto: AuthorCreateDTO, db: AsyncSession = Depends(get_db)):
    return await create_author(db, author_create_dto)

@router.get("/{author_id}", response_model=AuthorOutDTO)
async def get_author_endpoint(author_id: int, db: AsyncSession = Depends(get_db)):
    return await get_author_by_id(db, author_id)

@router.get("/", response_model=list[AuthorOutDTO])
async def get_authors_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_authors(db)

@router.put("/{author_id}", response_model=AuthorOutDTO)
async def update_author_endpoint(author_id: int, author_update_dto: AuthorUpdateDTO, db: AsyncSession = Depends(get_db)):
    return await update_author(db, author_id, author_update_dto)

@router.delete("/{author_id}")
async def delete_author_endpoint(author_id: int, db: AsyncSession = Depends(get_db)):
    await delete_author(db, author_id)
    return {"message": "Author deleted successfully"}
