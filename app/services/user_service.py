from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User
from sqlalchemy import select

async def get_all_users(db: AsyncSession):
    return await db.execute(select(User))