from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserUpdate


class UserDao:

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> User | None:
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list(db: AsyncSession) -> list[User]:
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def create(db: AsyncSession, user: User) -> User:
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def update(db: AsyncSession, req: UserUpdate) -> User:
        user_id = req.id
        user = await UserDao.get(db, user_id)
        if not user:
            raise ValueError("User not found")

        for field, value in req.model_dump(exclude_unset=True).items():
            setattr(user, field, value)

        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete(db: AsyncSession, user_id: int) -> None:
        await db.execute(
            delete(User).where(User.id == user_id)
        )
        await db.commit()
