import random
from typing import List

from faker.proxy import Faker
from sqlalchemy import select, insert

from app.core import db
from app.core.mappers.device_resource_mapper import device_resource_to_vo
from app.core.util import gen_id, now
from app.models.request_respones import QueryResourcesVO
from app.models.resources_model import DeviceResource

STATION_NAMES = [
    "城北变电站", "高新变电站", "东湖变电站", "西郊变电站"
]

AREA_NAMES = [
    "主控室", "开关区", "配电室", "围墙通道"
]

DEVICE_NAME_MAP = {
    "01": "智能网络高速球机",
    "02": "网络中速球机",
    "03": "网络固定摄像机",
    "04": "智能高速球机",
    "05": "中速球机",
    "06": "云台摄像机",
    "07": "固定摄像机",
    "08": "红外热成像摄像机",
    "09": "监拍装置",
    "10": "布控球",
    "11": "手持终端/单兵",
    "12": "智能安全帽",
    "13": "智能巡检机器人",
    "14": "无人机",
    "15": "移动采集设备",
    "16": "红外对射",
    "17": "红外双鉴",
    "18": "水浸探头",
    "19": "烟雾探测",
    "20": "温度探测",
    "21": "警笛",
    "22": "门禁控制器",
    "23": "电子围栏",
    "25": "震动监测",
    "26": "一键警报",
    "31": "温度传感器",
    "32": "湿度传感器",
    "33": "SF6浓度监测设备",
    "41": "数据存储设备",
    "42": "射频增强设备",
    "43": "光端机",
    "44": "网络延伸器",
    "45": "交换机",
    "46": "防火墙",
    "51": "工控机/板卡DVR",
    "52": "嵌入式DVR/NVS",
    "53": "IP Camera",
    "54": "综合接入设备",
    "55": "智能分析装置",
    "56": "人脸分析设备",
    "61": "灯光控制器",
    "62": "云镜控制器",
    "63": "告警控制器",
    "64": "视频切换控制器",
    "71": "赋值照明装置",
    "72": "时钟控制装置",
    "73": "视频解码设备",
    "74": "打印机",
    "75": "窗口采集设备",
    "76": "网口采集设备",
    "77": "综合接入装置"
}

DEVICE_TYPES = list(DEVICE_NAME_MAP.keys())


async def get_resource(pid, dev_type, protocol_type, status) -> List[QueryResourcesVO]:
    """查询资源"""
    async with db.AsyncSessionLocal() as session:

        stmt = select(DeviceResource)
        if pid:
            stmt = stmt.where(DeviceResource.pid == pid)

        if dev_type:
            stmt = stmt.where(DeviceResource.dev_type.in_(dev_type))

        if status:
            stmt = stmt.where(DeviceResource.status == status)

        stmt = stmt.order_by(DeviceResource.created_time.asc())

        result = await session.execute(stmt)
        resources = result.scalars().all()
        resources_vo = []
        if resources:
            for resource in resources:
                resources_vo.append(device_resource_to_vo(resource))
        return resources_vo


async def mock_device_resource():
    records = build_mock_records()

    stmt = insert(DeviceResource).values(records)

    async with db.AsyncSessionLocal() as session:
        await session.execute(stmt)
        await session.commit()

    return len(records)


def build_mock_records():
    """模拟资源数据"""
    fake = Faker("zh_CN")
    station_name = random.choice(STATION_NAMES)
    station_id = gen_id()
    records = []

    # 根节点
    records.append({
        "id": station_id,
        "text": "城北变电站",
        "dev_short_name": "城北站",
        "p_notes": fake.company(),
        "pid": None,
        "path": f"/{station_id}",
        "is_group": 1,
        "has_children": True,
        "children_count": 2,
        "dev_code": f"ST-{fake.random_number(5)}",
        "dev_type": "00",
        "status": 1
    })

    # 分组
    group_ids = []
    for area in ["主控室", "配电室"]:
        gid = gen_id()
        group_ids.append(gid)

        records.append({
            "id": gid,
            "text": area,
            "dev_short_name": area,
            "p_notes": fake.address(),
            "pid": station_id,
            "path": f"/{station_id}/{gid}",
            "is_group": 1,
            "has_children": True,
            "children_count": 3,
            "dev_code": f"AR-{fake.random_number(5)}",
            "dev_type": "00",
            "status": 1
        })

    # 设备
    for gid in group_ids:
        for i in range(3):
            records.append({
                "id": gen_id(),
                "text": f"网络摄像机-{i + 1}",
                "dev_short_name": f"IPC{i + 1}",
                "p_notes": fake.sentence(),
                "pid": gid,
                "path": f"/{station_id}/{gid}/{gen_id()}",
                "is_group": 0,
                "has_children": False,
                "children_count": 0,
                "dev_code": f"DEV-{fake.unique.random_number(6)}",
                "dev_type": "53",
                "status": random.choice([0, 1]),
                "lng": fake.longitude(),
                "lat": fake.latitude(),
                "is_check": True,
                "audio": random.choice([0, 1]),
                "created_time": now(),
                "updated_time": now()
            })

    return records
