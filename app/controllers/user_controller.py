from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.user_service import (
    register_user, login_user, get_user_by_id, update_user, delete_user, create_user
)
from app.dto.user_dto import (
    UserRegisterDTO, UserLoginDTO, UserUpdateDTO, UserOutDTO
)

router = APIRouter()

@router.post("/register", response_model=UserOutDTO)
async def register_user_endpoint(user_register_dto: UserRegisterDTO, db: AsyncSession = Depends(get_db)):
    return await register_user(db, user_register_dto)

@router.post("/login")
async def login_user_endpoint(user_login_dto: UserLoginDTO, db: AsyncSession = Depends(get_db)):
    return await login_user(db, user_login_dto)

@router.get("/{user_id}", response_model=UserOutDTO)
async def get_user_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_user_by_id(db, user_id)

@router.put("/{user_id}", response_model=UserOutDTO)
async def update_user_endpoint(user_id: int, user_update_dto: UserUpdateDTO, db: AsyncSession = Depends(get_db)):
    return await update_user(db, user_id, user_update_dto)

# Admin-specific routes
@router.delete("/{user_id}")
async def delete_user_endpoint(user_id: int, db: AsyncSession = Depends(get_db)):
    await delete_user(db, user_id)
    return {"message": "User deleted successfully"}

@router.post("/create", response_model=UserOutDTO)
async def create_user_endpoint(user_create_dto: UserRegisterDTO, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_create_dto)

