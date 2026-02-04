from datetime import datetime
from typing import Optional

from pydantic import Field

from app.models.base import CamelModel


class ToolBoxTalkCameraRelaBaseVO(CamelModel):
    camera_id: str = Field(..., description="布控球ID")
    tool_box_talk_id: Optional[str] = Field(None, description="站班会ID")
    province_code: Optional[str] = Field(None, description="省公司编码")
    sort_no: int = Field(0, description="排序号")


class ToolBoxTalkCameraRelaVO(ToolBoxTalkCameraRelaBaseVO):
    id: str = Field(..., description="主键ID")
    delete_flag: int = Field(..., description="删除状态")
    create_time: datetime = Field(..., description="创建时间")
    update_time: datetime = Field(..., description="更新时间")


class ToolBoxTalkCameraRelaCreateVO(ToolBoxTalkCameraRelaBaseVO):

    creater_id: str = Field(..., description="创建人")


class ToolBoxTalkCameraRelaUpdateVO(CamelModel):
    id: str = Field(..., description="主键ID")
    sort_no: Optional[int] = Field(None, description="排序号")
    updater_id: str = Field(..., description="更新人")
