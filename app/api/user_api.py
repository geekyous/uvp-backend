from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import ApiResponse, success
from app.vo.user import UserCreate, UserVO, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users")


@router.post("", response_model=UserVO)
async def create_user(req: UserCreate, db: AsyncSession = Depends(get_db)):
    return UserService.create(db, req)


@router.get("/{user_id}", response_model=ApiResponse[UserVO], )
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await UserService.get(db, user_id)
    return success(UserVO.model_validate(user))


@router.get("", response_model=list[UserVO])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await UserService.list(db)


@router.put("", response_model=UserVO)
async def update_user(req: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await UserService.update(db, req)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    await UserService.delete(db, user_id)
    return {"success": True}
