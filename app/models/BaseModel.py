from datetime import datetime
from typing import Optional, Dict, Any

from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import declared_attr

from app.core.db import Base


class BaseModel(Base):
    """基础模型(抽象类)"""
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now(), nullable=False, comment="创建时间")
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False, comment="更新时间")
    deleted_at = Column(DateTime, nullable=True, comment="删除时间（软删除）")

    @declared_attr
    def __tablename__(cls) -> str:
        """自动生成表名"""
        return cls.__name__.lower()

    def to_dict(self, exclude: Optional[list] = None) -> dict:
        """将模型转成字典
        :param exclude:要排除的字段列表
        :return 模型字典
        """
        result = {}
        exclude = exclude or []

        for column in self.__table__.columns:
            if column.name not in exclude:
                value = getattr(self, column.name)
                if isinstance(value, datetime):
                    result[column.name] = value.isoformat()
                else:
                    result[column.name] = value
        return result

    def update_from_dict(self, data: Dict[str, Any], exclude: Optional[list] = None):
        """从字典更新模型字段
        :param data 更新数据
        :param exclude:  要排除的字段列表
        """
        exclude = exclude or ["id", "created_at", "updated_at", "deleted_at"]

        for key, value in data.items():
            if hasattr(self, key) and key not in exclude and value is not None:
                setattr(self, key, value)
