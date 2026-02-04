from datetime import datetime
from typing import Optional

from pydantic import Field

from app.models.base import CamelModel


class CameraVO(CamelModel):
    """布控球 VO"""

    id: str = Field(..., title="主键ID")
    camera_name: Optional[str] = Field(None, title="布控球名称")
    camera_no: str = Field(..., title="布控球编码")

    province_code: Optional[str] = Field(None, title="省公司编码")

    creater_id: Optional[str] = Field(None, title="创建人")
    create_time: Optional[datetime] = Field(None, title="创建时间")

    updater_id: Optional[str] = Field(None, title="更新人")
    update_time: Optional[datetime] = Field(None, title="更新时间")

    delete_flag: int = Field(0, title="删除标识")
