from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, Field


class QueryResourcesVO(BaseModel):
    """查询资源树返回接口"""
    id: str = Field(..., description="资源id")
    text: str = Field(..., description="资源名称")
    devShortName: Optional[str] = Field(None, description="设备简称")
    pNotes: Optional[str] = Field(None, description="备注信息")
    pCode: Optional[str] = Field(None, description="父节点编码")
    url: Optional[str] = Field(None, description="资源链接")

    openType: Optional[int] = Field(
        None,
        description="资源打开方式"
    )

    pid: Optional[str] = Field(None, description="父节点ID")
    path: Optional[str] = Field(None, description="资源路径")

    type: Optional[int] = Field(
        None,
        description="资源类型",
        ge=0
    )

    isGroup: Optional[int] = Field(
        None,
        description="是否为分组(1：分组，0：设备)",
        ge=0,
        le=1
    )

    isAvailable: int = Field(
        ...,
        description="资源状态: 1-有效, 0-无效",
        ge=0,
        le=1
    )

    order: int = Field(..., description="展示顺序")

    hasChildren: bool = Field(..., description="是否有子节点: true-是, false-否")

    status: int = Field(
        ...,
        description="设备状态: 0-不在线, 1-在线, 2-不可用",
        ge=0,
        le=2
    )

    isOuternet: Optional[int] = Field(
        None,
        description="是否外网: 0-内网, 1-外网",
        ge=0,
        le=1
    )

    sDecodeTag: Optional[str] = Field(
        None,
        description="设备解码标签: 108-H265, 100-H264, 150-非标"
    )

    devCode: str = Field(..., description="设备编码")

    devType: str = Field(
        ...,
        description="""
            设备类型。
            01：智能网络高速球机;02：网络中速球机;03：网络固定摄像机;04：智能高速球机;05：中速球机;
            06：云台摄像机;07：固定摄像机;08：红外热成像摄像机;09：监拍装置;10：布控球;11：手持终端/单兵;
            12：智能安全帽;13：智能巡检机器人;14：无人机;15：移动采集设备;16：红外对射;17：红外双鉴;
            18：水浸探头;19：烟雾探测;20：温度探测;21：警笛;22：门禁控制器;23：电子围栏;25：震动监测;
            26：一键警报;31：温度传感器;32：湿度传感器;33：SF6浓度监测设备;41：数据存储设备;42：射频增强设备;
            43：光端机;44：网络延伸器;45：交换机;46：防火墙;51：工控机/板卡DVR;52：嵌入式DVR/NVS;53：IP Camera;
            54：综合接入设备;55：智能分析装置;56：人脸分析设备;61：灯光控制器;62：云镜控制器;63：告警控制器;
            64：视频切换控制器;71：赋值照明装置;72：时钟控制装置;73：视频解码设备;74：打印机;75：窗口采集设备;
            76：网口采集设备;77：综合接入装置""",
        example="09"
    )

    lng: Optional[Decimal] = Field(None, description="经度位置")
    lat: Optional[Decimal] = Field(None, description="纬度位置")

    childrenCount: int = Field(..., description="子节点数量", ge=0)

    gisPeerCode: Optional[str] = Field(None, description="GIS侧标识设备的编码")

    childNodes: Optional[List['QueryResourcesVO']] = Field(
        None,
        description="下级资源节点信息列表"
    )

    sysInfoCode: Optional[str] = Field(None, description="设备所属前端编码")
    dvrCode: Optional[str] = Field(None, description="dvr编码")

    isCheck: Optional[bool] = Field(None, description="设备是否关联dvr: true-是, false-否")

    fontTypeCode: Optional[str] = Field(
        None,
        description="电压等级: 01-35KV及其以下, 02-66KV, 03-110KV, 04-220V, "
                    "05-330KV, 06-500KV, 07-750KV及其以上, 10-其他"
    )

    peerId: Optional[str] = Field(None, description="协议编码")

    audio: Optional[int] = Field(
        None,
        description="是否包含音频: 0-否, 1-是",
        ge=0,
        le=1
    )
