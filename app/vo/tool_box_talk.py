from datetime import datetime, date
from typing import Optional

from pydantic import Field

from app.models.base import CamelModel


class ToolBoxTalkVO(CamelModel):
    """站班会 VO"""

    id: str = Field(..., title="主键ID", example="1234567890abcdef")
    off_online_flag: int = Field(..., title="离线标识", description="0-非离线，1-离线", example=0)

    prj_name: str = Field(..., title="项目名称", example="安徽500kV输电工程")
    prj_code: str = Field(..., title="项目编码", example="PRJ001")

    ticket_id: str = Field(..., title="作业票ID", example="TK123456")
    ticket_no: str = Field(..., title="作业票编号", example="ZY-20240101-001")

    re_assessment_risk_level: Optional[int] = Field(
        None, title="复测风险等级", description="1-5级", example=3
    )

    current_constr_headcount: int = Field(..., title="当日作业人数", example=12)
    construction_headcount: Optional[int] = Field(None, title="施工人数", example=10)

    work_start_time: Optional[datetime] = Field(None, title="作业开始时间")
    current_constr_date: date = Field(..., title="施工日期", example="2024-01-01")

    current_construction_status: Optional[str] = Field(
        None, title="施工状态", description="01-作业中；02-暂停中；03-作业完工", example="01"
    )

    work_overnight_flag: Optional[int] = Field(
        None, title="是否跨零点", description="0-否，1-是", example=0
    )

    tool_box_talk_address: Optional[str] = Field(None, title="站班会地址")
    tool_box_talk_longitude: Optional[str] = Field(None, title="经度", example="117.123456")
    tool_box_talk_latitude: Optional[str] = Field(None, title="纬度", example="31.123456")

    mc_work_site_id: Optional[str] = Field(None, title="最近作业部位ID")

    bidding_section_code: Optional[str] = Field(None, title="标段编码")
    bidding_section_name: Optional[str] = Field(None, title="标段名称")

    single_project_code: Optional[str] = Field(None, title="单项工程编码")
    single_project_name: Optional[str] = Field(None, title="单项工程名称")
    single_project_type: Optional[int] = Field(
        None, title="工程类型", description="1-变电工程；2-线路工程；3-电缆工程", example=1
    )

    constr_unified_social_credit_id: Optional[str] = Field(None, title="施工单位统一社会信用代码")
    construction_unit_name: Optional[str] = Field(None, title="施工单位名称")

    supervision_social_credit_code: Optional[str] = Field(None, title="监理单位统一社会信用代码")
    supervision_unit_name: Optional[str] = Field(None, title="监理单位名称")

    voltage_level: Optional[str] = Field(None, title="电压等级", example="500kV")

    huv_flag: Optional[int] = Field(
        0, title="特高压标识", description="0-常规工程，1-特高压", example=0
    )

    build_unit_code: Optional[str] = Field(None, title="建设管理单位编码")
    province_code: Optional[str] = Field(None, title="省公司编码")

    creater_id: str = Field(..., title="创建人ID")
    create_time: datetime = Field(..., title="创建时间")

    updater_id: str = Field(..., title="更新人ID")
    update_time: datetime = Field(..., title="更新时间")

    delete_flag: int = Field(0, title="删除标识", description="0-未删除，1-已删除")
