from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.user import User
from app.dto.user_dto import UserRegisterDTO, UserLoginDTO, UserUpdateDTO, UserOutDTO
from passlib.context import CryptContext

# For password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(db: AsyncSession, user_register_dto: UserRegisterDTO) -> UserOutDTO:
    hashed_password = pwd_context.hash(user_register_dto.password)
    user = User(username=user_register_dto.username, email=user_register_dto.email, hashed_password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserOutDTO.from_orm(user)

async def login_user(db: AsyncSession, user_login_dto: UserLoginDTO):
    result = await db.execute(select(User).filter_by(username=user_login_dto.username))
    user = result.scalars().first()
    if user and pwd_context.verify(user_login_dto.password, user.hashed_password):
        return {"message": "Login successful"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")

async def get_user_by_id(db: AsyncSession, user_id: int) -> UserOutDTO:
    result = await db.execute(select(User).filter_by(id=user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOutDTO.from_orm(user)

async def update_user(db: AsyncSession, user_id: int, user_update_dto: UserUpdateDTO) -> UserOutDTO:
    query = select(User).filter_by(id=user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update_dto.password:
        hashed_password = pwd_context.hash(user_update_dto.password)
        user_update_dto.password = hashed_password

    for var, value in vars(user_update_dto).items():
        setattr(user, var, value) if value is not None else None

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return UserOutDTO.from_orm(user)

async def delete_user(db: AsyncSession, user_id: int):
    query = select(User).filter_by(id=user_id)
    result = await db.execute(query)
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(user)
    await db.commit()

async def create_user(db: AsyncSession, user_register_dto: UserRegisterDTO) -> UserOutDTO:
    hashed_password = pwd_context.hash(user_register_dto.password)
    new_user = User(username=user_register_dto.username, email=user_register_dto.email, hashed_password=hashed_password, is_admin=True)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return UserOutDTO.from_orm(new_user)
