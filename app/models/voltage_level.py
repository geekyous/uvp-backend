from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class VoltageLevel(Base):
    """电压等级枚举表"""

    __tablename__ = "voltage_level"

    level_code: Mapped[str] = mapped_column(
        String(2), primary_key=True, comment="电压等级编码"
    )
    level_name: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="电压等级名称"
    )
