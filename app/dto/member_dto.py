from pydantic import BaseModel
from typing import Optional

class MemberBaseDTO(BaseModel):
    name: str
    contact_information: str
    permissions: str
    membership_status: str
    membership_period: int

class MemberCreateDTO(MemberBaseDTO):
    pass

class MemberUpdateDTO(BaseModel):
    name: Optional[str] = None
    contact_information: Optional[str] = None
    permissions: Optional[str] = None
    membership_status: Optional[str] = None
    membership_period: Optional[int] = None

class MemberOutDTO(MemberBaseDTO):
    id: int

    class Config:
        from_attributes = True
