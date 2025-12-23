from app.core.db import Base

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

class ApiCredential(Base):
    __tablename__ = "api_credential"

    id: Mapped[int] = mapped_column(primary_key=True)
    access_key: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    secret_key: Mapped[str] = mapped_column(String(128))
    status: Mapped[int] = mapped_column(Integer, default=1)
    expire_at: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime | None] = mapped_column(DateTime)
