from sqlalchemy import Column, Integer, String, Enum
from app.database import Base
import enum

class MembershipStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"

class Member(Base):
    __tablename__ = 'members'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_information = Column(String)
    permissions = Column(String) 
    membership_status = Column(Enum(MembershipStatus))
    membership_period = Column(Integer)
