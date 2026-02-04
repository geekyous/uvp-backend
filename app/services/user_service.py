from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.user_dao import UserDAO
from app.models.user import User
from app.vo.user import UserCreate, UserUpdate


class UserService:

    @staticmethod
    async def create(db: AsyncSession, req: UserCreate) -> User:
        user = User(**req.model_dump())
        return await UserDAO.create(db, user)

    @staticmethod
    async def update(db: AsyncSession, user_update: UserUpdate) -> User:
        return await UserDAO.update(db, user_update)

    @staticmethod
    async def delete(db: AsyncSession, user_id: int):
        await UserDAO.delete(db, user_id)

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> User:
        return await UserDAO.get(db, user_id)

    @staticmethod
    async def list(db: AsyncSession) -> list[User]:
        return await UserDAO.list_all(db)
