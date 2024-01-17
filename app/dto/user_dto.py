from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBaseDTO(BaseModel):
    username: str
    email: EmailStr

class UserRegisterDTO(UserBaseDTO):
    password: str

class UserLoginDTO(BaseModel):
    username: str
    password: str

class UserUpdateDTO(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserOutDTO(UserBaseDTO):
    id: int
    is_active: bool
    is_admin: bool
