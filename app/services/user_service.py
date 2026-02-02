from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.user_dao import UserDao
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserService:

    @staticmethod
    async def create(db: AsyncSession, req: UserCreate) -> User:
        user = User(**req.model_dump())
        return await UserDao.create(db, user)

    @staticmethod
    async def update(db: AsyncSession, user_update: UserUpdate) -> User:
        return await UserDao.update(db, user_update)

    @staticmethod
    async def delete(db: AsyncSession, user_id: int):
        await UserDao.delete(db, user_id)

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> User:
        return await UserDao.get(db, user_id)

    @staticmethod
    async def list(db: AsyncSession) -> list[User]:
        return await UserDao.list(db)
