from pydantic import BaseModel
from typing import Optional

class AuthorBaseDTO(BaseModel):
    name: str

class AuthorCreateDTO(AuthorBaseDTO):
    pass

class AuthorUpdateDTO(BaseModel):
    name: Optional[str] = None

class AuthorOutDTO(AuthorBaseDTO):
    id: int
