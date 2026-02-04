from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ToolBoxTalkCameraRela(Base):
    """
    站班会布控球关联表
    """
    __tablename__ = "toolboxtalk_camera_rela"

    # ================= 主键 =================
    id: Mapped[str] = mapped_column(
        String(32),
        primary_key=True,
        comment="主键ID"
    )

    # ================= 业务字段 =================
    camera_id: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        index=True,
        comment="布控球ID"
    )

    tool_box_talk_id: Mapped[Optional[str]] = mapped_column(
        String(32),
        nullable=True,
        index=True,
        comment="站班会ID"
    )

    province_code: Mapped[Optional[str]] = mapped_column(
        String(32),
        comment="省公司编码"
    )

    # ================= 审计字段 =================
    creater_id: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        comment="创建人"
    )

    create_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="创建时间"
    )

    updater_id: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        comment="更新人"
    )

    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        comment="更新时间"
    )

    # ================= 状态字段 =================
    delete_flag: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="删除状态 0未删除 1已删除"
    )

    sort_no: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="排序号"
    )
