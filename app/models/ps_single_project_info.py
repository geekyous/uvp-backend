from datetime import datetime, date
from decimal import Decimal

from sqlalchemy import String, Integer, DateTime, Date, Text, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class PsSingleProjectInfo(Base):
    """单项工程信息表"""

    __tablename__ = "ps_single_project_info"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, comment="主键")

    build_unit_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="建设管理单位编码"
    )
    build_unit_name: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="建设管理单位名称"
    )
    area: Mapped[str | None] = mapped_column(String(8), nullable=True, comment="区域")
    single_project_type: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="单项工程类型"
    )
    single_project_prer_type: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="单项工程预规类型"
    )
    single_project_details_type: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="单项工程明细类型"
    )
    safety_project_status: Mapped[str | None] = mapped_column(
        String(128), nullable=True, comment="安全工程状态"
    )
    is_work: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="是否在施"
    )
    is_stop: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="是否停工"
    )
    scale: Mapped[str | None] = mapped_column(Text, nullable=True, comment="项目规模")
    voltage_level: Mapped[str | None] = mapped_column(
        String(12), nullable=True, comment="电压等级"
    )
    constr_nature: Mapped[str | None] = mapped_column(
        String(24), nullable=True, comment="建设性质"
    )
    project_num: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="项目编号"
    )
    safety_code: Mapped[str | None] = mapped_column(
        String(128), nullable=True, comment="安全编码"
    )
    parent_name: Mapped[str | None] = mapped_column(
        String(128), nullable=True, comment="隶属大项工程名称"
    )
    prj_code: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="隶属大项工程编码"
    )
    construction_line_length: Mapped[Decimal | None] = mapped_column(
        Numeric(17, 3), nullable=True, comment="建设线路长度"
    )
    constr_transformer_capacity: Mapped[Decimal | None] = mapped_column(
        Numeric(17, 3), nullable=True, comment="建设变电容量"
    )
    production_line_length: Mapped[Decimal | None] = mapped_column(
        Numeric(17, 3), nullable=True, comment="投产线路长度"
    )
    prod_trans_capacity: Mapped[Decimal | None] = mapped_column(
        Numeric(17, 3), nullable=True, comment="投产变电容量"
    )
    name: Mapped[str | None] = mapped_column(
        String(128), nullable=True, comment="单项工程名称"
    )
    safety_director: Mapped[str | None] = mapped_column(
        String(512), nullable=True, comment="安全总监(SM2密文)"
    )
    construction_organization: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="建设单位"
    )
    supervisor_organization: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="监理单位"
    )
    builder: Mapped[str | None] = mapped_column(
        String(64), nullable=True, comment="施工单位"
    )
    location_province: Mapped[str | None] = mapped_column(
        String(16), nullable=True, comment="单项所在省编码"
    )
    location_province_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="单项所在省名称"
    )
    location_municipality: Mapped[str | None] = mapped_column(
        String(16), nullable=True, comment="单项所在市编码"
    )
    location_municipality_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="单项所在市名称"
    )
    location_area: Mapped[str | None] = mapped_column(
        String(16), nullable=True, comment="单项所在区/县编码"
    )
    location_area_name: Mapped[str | None] = mapped_column(
        String(255), nullable=True, comment="单项所在区/县名称"
    )
    planned_start_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="计划开工时间"
    )
    actual_start_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="实际开工时间"
    )
    planned_commissioning_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="计划投产时间"
    )
    actual_commissioning_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="实际投产时间"
    )
    planned_completion_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="计划竣工时间"
    )
    actual_completion_time: Mapped[date | None] = mapped_column(
        Date, nullable=True, comment="实际竣工时间"
    )
    week_plan_range: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="次周计划日期范围"
    )
    construction_status: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="在建状态：默认0：0：施工；1：暂停"
    )
    status_from_weekly: Mapped[int | None] = mapped_column(
        Integer, nullable=True, comment="工程状态"
    )
    basic_data: Mapped[int] = mapped_column(
        Integer, server_default="0", comment="基础数据 1 基础数据 0 非基础数据"
    )
    sync_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, comment="数据同步时间"
    )
    sync_source: Mapped[str] = mapped_column(
        String(16), nullable=False, comment="数据同步来源"
    )
    session: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="同步session"
    )
    created_by: Mapped[str] = mapped_column(
        String(32), nullable=False, comment="创建人"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, comment="创建时间"
    )
    updated_by: Mapped[str | None] = mapped_column(
        String(32), nullable=True, comment="最近一次更新人"
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, comment="最近一次更新时间"
    )
    ext_id: Mapped[str | None] = mapped_column(
        String(36), nullable=True, comment="外部Id"
    )
    src_flag: Mapped[str | None] = mapped_column(
        String(512), nullable=True, comment="数据来源标记"
    )
    enable_modify_week_plan: Mapped[str] = mapped_column(
        String(32), server_default="1", comment="是否可修改周计划项目规模"
    )
    remarks: Mapped[str | None] = mapped_column(
        Text, nullable=True, comment="备注"
    )
