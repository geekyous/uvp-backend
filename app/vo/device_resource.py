from datetime import datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import Field

from app.models.base import CamelModel

class QueryResource(CamelModel):
    """查询资源树接口参数"""
    pid: str = Field(None, description="父节点id。不传值则返回根节点下的资源列表")

    devType: List = Field(None, description="""
    设备类型。
    01：智能网络高速球机;02：网络中速球机;03：网络固定摄像机;04：智能高速球机;05：中速球机;
    06：云台摄像机;07：固定摄像机;08：红外热成像摄像机;09：监拍装置;10：布控球;11：手持终端/单兵;
    12：智能安全帽;13：智能巡检机器人;14：无人机;15：移动采集设备;16：红外对射;17：红外双鉴;
    18：水浸探头;19：烟雾探测;20：温度探测;21：警笛;22：门禁控制器;23：电子围栏;25：震动监测;
    26：一键警报;31：温度传感器;32：湿度传感器;33：SF6浓度监测设备;41：数据存储设备;42：射频增强设备;
    43：光端机;44：网络延伸器;45：交换机;46：防火墙;51：工控机/板卡DVR;52：嵌入式DVR/NVS;53：IP Camera;
    54：综合接入设备;55：智能分析装置;56：人脸分析设备;61：灯光控制器;62：云镜控制器;63：告警控制器;
    64：视频切换控制器;71：赋值照明装置;72：时钟控制装置;73：视频解码设备;74：打印机;75：窗口采集设备;
    76：网口采集设备;77：综合接入装置
    注：此参数在查场景下的设备时有效，不传则不过滤。""")

    protocolType: int = Field(None, description="""
    协议类型。
    0：I1；1：非标；2：企标2014；3：企标2020；4：国标2016；
    注：此参数在查场景下的设备时有效，不传则不过滤。""")

    status: int = Field(None, description="""
    设备状态。
    0:不在线;1:在线;2:不可用。
    注：此参数在查场景下的设备时有效，不传则不过滤。""")

class DeviceResourceVO(CamelModel):
    """资源信息 VO"""

    id: str = Field(..., title="资源ID")
    text: str = Field(..., title="资源名称")

    dev_short_name: Optional[str] = Field(None, title="设备简称")
    p_notes: Optional[str] = Field(None, title="备注")

    p_code: Optional[str] = Field(None, title="父节点编码")
    url: Optional[str] = Field(None, title="资源链接")

    open_type: Optional[int] = Field(0, title="打开方式")

    pid: Optional[str] = Field(None, title="父节点ID")
    path: Optional[str] = Field(None, title="资源路径")

    type: Optional[int] = Field(None, title="资源类型")

    is_group: int = Field(0, title="是否分组")
    is_available: int = Field(1, title="是否有效")

    order: int = Field(0, title="展示顺序")

    has_children: bool = Field(False, title="是否有子节点")

    status: int = Field(0, title="设备状态")

    is_outernet: Optional[int] = Field(0, title="是否外网")

    s_decode_tag: Optional[str] = Field(None, title="解码标签")

    dev_code: str = Field(..., title="设备编码")
    dev_type: str = Field(..., title="设备类型")

    lng: Optional[Decimal] = Field(None, title="经度")
    lat: Optional[Decimal] = Field(None, title="纬度")

    children_count: Optional[int] = Field(0, title="子节点数量")

    gis_peer_code: Optional[str] = Field(None, title="GIS编码")
    sys_info_code: Optional[str] = Field(None, title="前端编码")
    dvr_code: Optional[str] = Field(None, title="DVR编码")

    is_check: Optional[bool] = Field(False, title="是否关联DVR")

    font_type_code: Optional[str] = Field(None, title="电压等级")
    peer_id: Optional[str] = Field(None, title="协议编码")

    audio: Optional[int] = Field(0, title="是否包含音频")

    created_time: Optional[datetime] = Field(None, title="创建时间")
    updated_time: Optional[datetime] = Field(None, title="更新时间")
