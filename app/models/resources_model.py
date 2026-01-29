from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import String, Integer, Boolean, Text, DateTime, DECIMAL, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class DeviceResource(Base):
    """资源信息实体类"""
    __tablename__ = "device_resource"

    # 主键和基础信息
    id: Mapped[str] = mapped_column(String(64), primary_key=True, comment="资源ID")
    text: Mapped[str] = mapped_column(String(255), nullable=False, comment="资源名称")
    dev_short_name: Mapped[Optional[str]] = mapped_column(String(100), comment="设备简称")
    p_notes: Mapped[Optional[str]] = mapped_column(Text, comment="备注信息")
    p_code: Mapped[Optional[str]] = mapped_column(String(100), comment="父节点编码")
    url: Mapped[Optional[str]] = mapped_column(String(500), comment="资源链接")
    open_type: Mapped[Optional[int]] = mapped_column(Integer, default=0, comment="资源打开方式")

    # 树形结构相关
    pid: Mapped[Optional[str]] = mapped_column(String(50), comment="父节点ID")
    path: Mapped[Optional[str]] = mapped_column(String(1000), comment="资源路径")
    type: Mapped[Optional[int]] = mapped_column(Integer, comment="资源类型")

    # 状态和属性
    is_group: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="是否为分组(1：分组，0：设备)")
    is_available: Mapped[int] = mapped_column(Integer, nullable=False, default=1, comment="资源状态 1:有效；0:无效")
    order: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="展示顺序")
    has_children: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False,
                                               comment="是否有子节点 true:是；false:否")
    status: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="设备状态 0:不在线；1:在线；2:不可用")
    is_outernet: Mapped[Optional[int]] = mapped_column(Integer, default=0, comment="是否外网 0:内网；1:外网")

    # 设备相关
    s_decode_tag: Mapped[Optional[str]] = mapped_column(String(10), comment="设备解码标签 108:H265；100:H264；150:非标")
    dev_code: Mapped[str] = mapped_column(String(100), nullable=False, comment="设备编码")
    dev_type: Mapped[str] = mapped_column(String(2), nullable=False, comment="设备类型")

    # 地理位置
    lng: Mapped[Optional[Decimal]] = mapped_column(DECIMAL(10, 6), comment="经度位置")
    lat: Mapped[Optional[Decimal]] = mapped_column(DECIMAL(10, 6), comment="纬度位置")
    tower_id: Mapped[Optional[str]] = mapped_column(String(32), comment="杆塔Id")
    audio: Mapped[Optional[int]] = mapped_column(Integer, default=0, comment="是否包含音频，0：否，1：是")

    # 统计和关联
    children_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="子节点数量")
    online_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment="在线点数量")
    gis_peer_code: Mapped[Optional[str]] = mapped_column(String(100), comment="GIS侧标识设备的编码")
    plat_code: Mapped[Optional[str]] = mapped_column(String(100), comment="平台编码")
    resource_attr: Mapped[Optional[str]] = mapped_column(String(100), comment="资源属性")
    resource_type: Mapped[Optional[str]] = mapped_column(String(100), comment="资源类型。1:区域；2:场景；3:专业")
    protocol_type: Mapped[Optional[str]] = mapped_column(String(16),
                                                         comment="协议类型 0：I1；1：非标；2：企标2014；3：企标2020；4：国标2016；")

    sys_info_code: Mapped[Optional[str]] = mapped_column(String(100), comment="设备所属前端编码")
    dvr_code: Mapped[Optional[str]] = mapped_column(String(100), comment="dvr编码")
    is_check: Mapped[Optional[bool]] = mapped_column(Boolean, default=False, comment="设备是否关联dvr true:是；false:否")
    self_data: Mapped[Optional[str]] = mapped_column(String, comment="")
    socre: Mapped[Optional[float]] = mapped_column(Float, comment="")
    coordinate: Mapped[Optional[str]] = mapped_column(String(100), comment="")
    use_status: Mapped[Optional[str]] = mapped_column(String(10), comment="")

    # 其他信息
    font_type_code: Mapped[Optional[str]] = mapped_column(String(2), comment="电压等级")
    peer_id: Mapped[Optional[str]] = mapped_column(String(50), comment="协议编码")

    # 时间戳
    created_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        default=datetime.now,
        comment="创建时间"
    )
    updated_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        comment="更新时间"
    )

    def to_dict(self):
        """转换为字典（方便序列化）"""
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(value, Decimal):
                value = float(value)
            elif isinstance(value, datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            result[column.name] = value
        return result


class DeviceType(Base):
    """设备类型枚举实体类"""
    __tablename__ = "device_type"

    type_code: Mapped[str] = mapped_column(String(2), primary_key=True, comment="设备类型编码")
    type_name: Mapped[str] = mapped_column(String(50), nullable=False, comment="设备类型名称")
    description: Mapped[Optional[str]] = mapped_column(String(200), comment="类型描述")

    def __repr__(self) -> str:
        return f"<DeviceType(type_code={self.type_code}, type_name={self.type_name})>"


class VoltageLevel(Base):
    """电压等级枚举实体类"""
    __tablename__ = "voltage_level"

    level_code: Mapped[str] = mapped_column(String(2), primary_key=True, comment="电压等级编码")
    level_name: Mapped[str] = mapped_column(String(50), nullable=False, comment="电压等级名称")

    def __repr__(self) -> str:
        return f"<VoltageLevel(level_code={self.level_code}, level_name={self.level_name})>"
