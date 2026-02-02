
from sqlalchemy import Column, Integer, String
from app.models.base import Base, TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String(64), nullable=False)
    email = Column(String(128), nullable=False)
