from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class DeviceType(Base):
    """设备类型枚举表"""

    __tablename__ = "device_type"

    type_code: Mapped[str] = mapped_column(
        String(2), primary_key=True, comment="设备类型编码"
    )
    type_name: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="设备类型名称"
    )
    description: Mapped[str | None] = mapped_column(
        String(200), nullable=True, comment="类型描述"
    )
