from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.models.user_model import User
from app.services import user_service
from app.schemas.user_schema import UserRead

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/", response_model=list[UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await user_service.get_all_users(db)