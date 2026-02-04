from datetime import datetime

from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Camera(Base):
    __tablename__ = "camera"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, comment="主键ID")

    camera_name: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="布控球名称"
    )
    camera_no: Mapped[str] = mapped_column(
        String(64), nullable=False, comment="布控球编码"
    )

    province_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="省公司编码"
    )

    creater_id: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="创建人"
    )
    create_time: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="创建时间"
    )

    updater_id: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="更新人"
    )
    update_time: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="更新时间"
    )

    delete_flag: Mapped[int] = mapped_column(
        Integer, server_default="0", comment="删除标识：0-未删除；1-已删除"
    )
