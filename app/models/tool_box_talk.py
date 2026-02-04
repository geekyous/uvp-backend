from datetime import datetime, date

from sqlalchemy import Index, String, Integer, DateTime, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ToolBoxTalk(Base):
    """站班会实体类"""

    __tablename__ = "tool_box_talk"

    __table_args__ = (
        # 复测风险等级 + 施工日期
        Index(
            "daily_meeting_risk_level_reassessment_current_constr_date_index",
            "re_assessment_risk_level",
            "current_constr_date",
        ),
        # 站班会统计分析索引
        Index(
            "daily_meeting_statistics_index",
            "single_project_code",
            "single_project_name",
            "prj_code",
            "build_unit_code",
        ),
        # 风险等级 + 状态 + 日期
        Index(
            "daily_meeting_count_index",
            "re_assessment_risk_level",
            "current_construction_status",
            "current_constr_date",
        ),
        # 日期 + 删除标识
        Index(
            "tool_box_talk_current_constr_date_delete_flag_index",
            "current_constr_date",
            "delete_flag",
        ),

        # 作业票跳转站班会
        Index(
            "tool_box_talk_ticket_id_delete_flag_index",
            "ticket_id",
            "delete_flag",
        ),

        # 标段编码
        Index(
            "tool_box_talk_bidding_section_code",
            "bidding_section_code",
        ),
        # 建设单位 + 日期 + 删除 + 特高压
        Index(
            "tool_box_talk_build_current_del_huv_index",
            "build_unit_code",
            "current_constr_date",
            "delete_flag",
            "huv_flag",
        ),

        # 作业票ID
        Index(
            "tool_box_talk_ticket_id_index",
            "ticket_id",
        ),

        # 日期 + 删除 + 特高压 + 省公司 + 建设单位
        Index(
            "tool_box_talk_current_del_huv_index",
            "current_constr_date",
            "delete_flag",
            "huv_flag",
            "province_code",
            "build_unit_code",
        ),

    )

    id: Mapped[str] = mapped_column(String(32), primary_key=True, comment="主键ID")

    off_online_flag: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="离线标识：0-非离线，1-离线"
    )

    prj_name: Mapped[str] = mapped_column(
        String(255), nullable=False, comment="项目名称"
    )

    prj_code: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="项目编码"
    )

    ticket_id: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="作业票id"
    )

    ticket_no: Mapped[str] = mapped_column(
        String(128), nullable=False, comment="作业票编号"
    )

    re_assessment_risk_level: Mapped[int | None] = mapped_column(
        Integer, comment="复测风险等级（1~5）"
    )

    current_constr_headcount: Mapped[int] = mapped_column(
        Integer, nullable=False, comment="当日作业人数"
    )

    construction_headcount: Mapped[int | None] = mapped_column(
        Integer, comment="施工人数"
    )

    work_start_time: Mapped[datetime | None] = mapped_column(
        DateTime, comment="作业开始时间"
    )

    current_constr_date: Mapped[date] = mapped_column(
        Date, nullable=False, comment="施工日期"
    )

    current_construction_status: Mapped[str | None] = mapped_column(
        String(8), comment="当日施工状态：01-作业中；02-暂停中；03-作业完工"
    )

    work_overnight_flag: Mapped[int | None] = mapped_column(
        Integer, comment="是否跨零点作业：0-否；1-是"
    )

    tool_box_talk_address: Mapped[str | None] = mapped_column(
        String(480), comment="站班会地址"
    )

    tool_box_talk_longitude: Mapped[str | None] = mapped_column(
        String(480), comment="站班会经度"
    )

    tool_box_talk_latitude: Mapped[str | None] = mapped_column(
        String(480), comment="站班会纬度"
    )

    mc_work_site_id: Mapped[str | None] = mapped_column(
        String(32), comment="最近作业部位ID"
    )

    bidding_section_code: Mapped[str | None] = mapped_column(
        String(32), comment="标段编码"
    )

    bidding_section_name: Mapped[str | None] = mapped_column(
        String(255), comment="标段名称"
    )

    single_project_code: Mapped[str | None] = mapped_column(
        String(32), comment="单项工程编码"
    )

    single_project_name: Mapped[str | None] = mapped_column(
        String(255), comment="单项工程名称"
    )

    single_project_type: Mapped[int | None] = mapped_column(
        Integer, comment="工程类型：1-变电；2-线路；3-电缆"
    )

    constr_unified_social_credit_id: Mapped[str | None] = mapped_column(
        String(18), comment="施工单位统一社会信用代码"
    )

    construction_unit_name: Mapped[str | None] = mapped_column(
        String(100), comment="施工单位名称"
    )

    supervision_social_credit_code: Mapped[str | None] = mapped_column(
        String(256), comment="监理单位统一社会信用代码"
    )

    supervision_unit_name: Mapped[str | None] = mapped_column(
        String(256), comment="监理单位名称"
    )

    voltage_level: Mapped[str | None] = mapped_column(
        String(12), comment="电压等级"
    )

    huv_flag: Mapped[int] = mapped_column(
        Integer, default=0, comment="0-常规工程；1-特高压"
    )

    build_unit_code: Mapped[str | None] = mapped_column(
        String(32), comment="建设管理单位编码"
    )

    province_code: Mapped[str | None] = mapped_column(
        String(32), comment="省公司编码"
    )

    creater_id: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="创建人"
    )

    create_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, comment="创建时间"
    )

    updater_id: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="更新人"
    )

    update_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, comment="更新时间"
    )

    delete_flag: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, comment="删除标识：0-未删除；1-已删除"
    )
