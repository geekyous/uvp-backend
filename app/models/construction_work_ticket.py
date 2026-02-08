from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ConstructionWorkTicket(Base):
    """施工作业票表"""

    __tablename__ = "construction_work_ticket"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, comment="主键ID")

    ticket_type: Mapped[str] = mapped_column(
        String(2), nullable=False, comment="作业票类型：A-A票；B-B票"
    )
    ticket_no: Mapped[str | None] = mapped_column(
        String(128), nullable=True, comment="作业票编号"
    )
    ticket_name: Mapped[str] = mapped_column(
        String(128), nullable=False, comment="作业票名称"
    )
    bidding_section_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="标段编码"
    )
    bidding_section_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="标段名称"
    )
    single_project_type: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="单项工程类型：1-变电工程；2-线路工程；3-电缆工程"
    )
    single_project_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="单项工程编码"
    )
    single_project_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="单项工程名称"
    )
    team_id: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="班组ID"
    )
    working_team_name: Mapped[str] = mapped_column(
        String(128), nullable=False, comment="作业班组名称"
    )
    construction_headcount: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="施工人数"
    )
    planned_start_date: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="计划开始时间"
    )
    planned_end_date: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="计划结束时间"
    )
    start_time: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="开始时间"
    )
    end_time: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="结束时间"
    )
    assessment_risk_level: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="初勘风险等级：2；3；4；5"
    )
    re_assessment_risk_level: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="复测风险等级：2；3；4；5"
    )
    ticket_status: Mapped[str] = mapped_column(
        String(8), nullable=False, comment="作业票状态：01-撤回；02-驳回；03-提交审核中；04-待执行；05-执行中；06-已结束；07-作废；08-删除"
    )
    current_construction_status: Mapped[str | None] = mapped_column(
        String(8), nullable=True, comment="当日施工状态：01-作业中；02-暂停中；03-作业完工"
    )
    audit_hierarchy: Mapped[str | None] = mapped_column(
        String(8), nullable=True, comment="审批层级：01-班组；02-施工；03-监理"
    )
    issue_type: Mapped[str | None] = mapped_column(
        String(8), nullable=True, comment="签发类型：01-审核签发；02-自动签发"
    )
    issue_date: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="签发日期"
    )
    priority: Mapped[str | None] = mapped_column(
        String(8), nullable=True, comment="优先级"
    )
    build_unit_code: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="建设管理单位编码"
    )
    province_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="省公司编码"
    )
    remark: Mapped[str | None] = mapped_column(
        String(480), nullable=True, comment="备注"
    )
    huv_flag: Mapped[int] = mapped_column(
        Integer, server_default="0", comment="0:常规工程 1:特高压"
    )
    voltage_level: Mapped[str | None] = mapped_column(
        String(12), nullable=True, comment="电压等级"
    )
    construction_unit_name: Mapped[str | None] = mapped_column(
        String(256), nullable=True, comment="施工单位名称"
    )
    construction_social_credit_code: Mapped[str | None] = mapped_column(
        String(256), nullable=True, comment="施工单位统一社会信用代码"
    )
    supervision_unit_name: Mapped[str | None] = mapped_column(
        String(256), nullable=True, comment="监理单位"
    )
    supervision_social_credit_code: Mapped[str | None] = mapped_column(
        String(256), nullable=True, comment="监理单位统一社会信用代码"
    )
    creater_id: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="创建人"
    )
    create_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, comment="创建时间"
    )
    updater_id: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="更新人"
    )
    update_time: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="更新时间"
    )
    delete_flag: Mapped[int] = mapped_column(
        Integer, server_default="0", comment="删除状态：0未删除，1已删除"
    )
