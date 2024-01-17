from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.services.member_service import create_member, get_members, update_member, delete_member
from app.dto.member_dto import MemberCreateDTO, MemberUpdateDTO, MemberOutDTO

router = APIRouter()

@router.post("/", response_model=MemberOutDTO)
async def create_member_endpoint(member_create_dto: MemberCreateDTO, db: AsyncSession = Depends(get_db)):
    return await create_member(db, member_create_dto)

@router.get("/", response_model=list[MemberOutDTO])
async def get_members_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_members(db)

@router.put("/{member_id}", response_model=MemberOutDTO)
async def update_member_endpoint(member_id: int, member_update_dto: MemberUpdateDTO, db: AsyncSession = Depends(get_db)):
    updated_member = await update_member(db, member_id, member_update_dto)
    if updated_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return updated_member

@router.delete("/{member_id}")
async def delete_member_endpoint(member_id: int, db: AsyncSession = Depends(get_db)):
    await delete_member(db, member_id)
    return {"message": "Member deleted successfully"}