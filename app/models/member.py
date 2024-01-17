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
    permissions = Column(String)  # This can be expanded or modified based on your auth system
    membership_status = Column(Enum(MembershipStatus))
    membership_period = Column(Integer)  # Assuming membership period is in days
