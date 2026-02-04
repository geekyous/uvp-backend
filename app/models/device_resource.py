from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    Boolean,
    DateTime,
    Numeric,
    text as sql_text
)

from app.models.base import Base


class DeviceResource(Base):
    __tablename__ = "device_resource"

    id = Column(String(64), primary_key=True, comment="资源ID")

    text = Column(String(255), nullable=False)

    dev_short_name = Column(String(100))
    p_notes = Column(Text)

    p_code = Column(String(100))
    url = Column(String(500))

    open_type = Column(Integer, server_default="0")

    pid = Column(String(50))
    path = Column(String(1000))

    type = Column(Integer)

    is_group = Column(Integer, nullable=False, server_default="0")
    is_available = Column(Integer, nullable=False, server_default="1")

    # ⚠️ order 是关键字，ORM改名
    order = Column("order", Integer, nullable=False, server_default="0")

    has_children = Column(Boolean, nullable=False, server_default=sql_text("0"))

    status = Column(Integer, nullable=False, server_default="0")

    is_outernet = Column(Integer, server_default="0")

    s_decode_tag = Column(String(10))

    dev_code = Column(String(100), nullable=False)
    dev_type = Column(String(2), nullable=False)

    lng = Column(Numeric(10, 6))
    lat = Column(Numeric(10, 6))

    children_count = Column(Integer, server_default="0")

    gis_peer_code = Column(String(100))
    sys_info_code = Column(String(100))
    dvr_code = Column(String(100))

    is_check = Column(Boolean, server_default=sql_text("0"))

    font_type_code = Column(String(2))
    peer_id = Column(String(50))

    audio = Column(Integer, server_default="0")

    created_time = Column(
        DateTime,
        server_default=sql_text("CURRENT_TIMESTAMP")
    )

    updated_time = Column(
        DateTime,
        server_default=sql_text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
