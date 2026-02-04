from __future__ import annotations

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.vo.user import UserUpdate


class UserDAO:
    """用户数据访问对象"""

    @staticmethod
    async def get(db: AsyncSession, user_id: int) -> User | None:
        """根据ID查询用户"""
        result = await db.execute(
            select(User).where(User.id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def list(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[User]:
        """查询用户列表"""
        result = await db.execute(
            select(User).offset(skip).limit(limit)
        )
        return list(result.scalars().all())

    @staticmethod
    async def list_all(db: AsyncSession) -> list[User]:
        """查询所有用户"""
        result = await db.execute(select(User))
        return list(result.scalars().all())

    @staticmethod
    async def create(db: AsyncSession, user: User) -> User:
        """创建用户"""
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def update(db: AsyncSession, req: UserUpdate) -> User:
        """更新用户"""
        user_id = req.id
        user = await UserDAO.get(db, user_id)
        if not user:
            raise ValueError("User not found")

        for field, value in req.model_dump(exclude_unset=True).items():
            setattr(user, field, value)

        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def update_by_id(db: AsyncSession, user_id: int, data: dict) -> None:
        """根据ID更新用户"""
        stmt = update(User).where(User.id == user_id).values(**data)
        await db.execute(stmt)
        await db.flush()

    @staticmethod
    async def delete(db: AsyncSession, user_id: int) -> None:
        """删除用户"""
        await db.execute(
            delete(User).where(User.id == user_id)
        )
        await db.commit()

    @staticmethod
    async def delete_by_id(db: AsyncSession, user_id: int) -> None:
        """根据ID删除用户（不提交）"""
        stmt = delete(User).where(User.id == user_id)
        await db.execute(stmt)
        await db.flush()
