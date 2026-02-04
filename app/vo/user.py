from app.models.base import CamelModel


class UserCreate(CamelModel):
    user_name: str
    email: str


class UserUpdate(CamelModel):
    id: int
    user_name: str | None = None
    email: str | None = None


class UserVO(CamelModel):
    id: int
    user_name: str
    email: str
