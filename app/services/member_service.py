from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from app.models.member import Member
from app.dto.member_dto import MemberCreateDTO, MemberUpdateDTO, MemberOutDTO

async def create_member(db: AsyncSession, member_create_dto: MemberCreateDTO) -> MemberOutDTO:
    member = Member(**member_create_dto.dict())
    db.add(member)
    await db.commit()
    await db.refresh(member)
    return MemberOutDTO.from_orm(member)

async def get_members(db: AsyncSession) -> list[MemberOutDTO]:
    result = await db.execute(select(Member))
    members = result.scalars().all()
    return [MemberOutDTO.from_orm(member) for member in members]

async def update_member(db: AsyncSession, member_id: int, member_update_dto: MemberUpdateDTO) -> MemberOutDTO:
    result = await db.execute(select(Member).where(Member.id == member_id))
    member = result.scalars().first()
    if not member:
        return None
    update_data = member_update_dto.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(member, key, value) if value is not None else None
    await db.commit()
    await db.refresh(member)
    return MemberOutDTO.from_orm(member)
    
async def delete_member(db: AsyncSession, member_id: int):
    query = select(Member).filter_by(id=member_id)
    result = await db.execute(query)
    member = result.scalars().first()
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")

    await db.delete(member)
    await db.commit()