import uuid
from datetime import datetime, date
from typing import Dict, Any, List
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.camera_dao import CameraDAO
from app.dao.device_resource_dao import DeviceResourceDAO
from app.dao.device_type_dao import DeviceTypeDAO
from app.dao.ps_single_project_info_dao import PsSingleProjectInfoDAO
from app.dao.tool_box_talk_dao import ToolBoxTalkDAO
from app.dao.toolboxtalk_camera_rela_dao import ToolBoxTalkCameraRelaDAO
from app.dao.voltage_level_dao import VoltageLevelDAO
from app.models.camera import Camera
from app.models.camera_rela import ToolBoxTalkCameraRela
from app.models.device_resource import DeviceResource
from app.models.tool_box_talk import ToolBoxTalk


class TestDataService:
    """测试数据生成服务"""

    @staticmethod
    async def generate_test_data(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        生成测试数据

        Args:
            db: 数据库会话
            project_limit: 使用的项目数量限制

        Returns:
            生成结果统计
        """
        result = {
            "device_resources": 0,
            "cameras": 0,
            "tool_box_talks": 0,
            "relations": 0,
            "projects_used": []
        }

        # 1. 获取真实项目数据
        projects = await PsSingleProjectInfoDAO.list_all(db, limit=project_limit)
        if not projects:
            raise ValueError("未找到单项工程信息，请先导入ps_single_project_info数据")

        # 2. 获取布控球设备类型
        device_type = await DeviceTypeDAO.get_by_code(db, "10")  # 布控球
        if not device_type:
            raise ValueError("未找到布控球设备类型（type_code=10）")

        # 3. 创建根节点
        root_id = f"root_{uuid.uuid4().hex[:8]}"
        root = DeviceResource(
            id=root_id,
            text="国网测试数据根节点",
            dev_code=f"ROOT_{datetime.now().strftime('%Y%m%d')}",
            dev_type="00",
            pid=None,
            path=f"/{root_id}",
            type=0,
            is_group=1,
            has_children=True,
            status=1,
            children_count=len(projects),
            order=0,
            is_available=1
        )
        db.add(root)
        result["device_resources"] += 1

        # 4. 为每个项目生成数据
        for idx, project in enumerate(projects, start=1):
            # 4.1 创建项目节点
            proj_id = f"proj_{uuid.uuid4().hex[:8]}"
            project_node = DeviceResource(
                id=proj_id,
                text=project.name or f"测试项目{idx}",
                dev_code=project.id,
                dev_type="02",  # 项目类型
                pid=root_id,
                path=f"/{root_id}/{proj_id}",
                type=2,
                is_group=1,
                has_children=True,
                status=1,
                children_count=0,  # 稍后更新
                order=idx,
                is_available=1
            )
            db.add(project_node)
            result["device_resources"] += 1

            # 4.2 生成布控球设备（每个项目3-5个）
            camera_count = min(3 + idx, 5)
            cameras_for_project = []

            for cam_idx in range(1, camera_count + 1):
                # 生成设备资源中的布控球
                camera_dev_id = f"camera_dev_{uuid.uuid4().hex[:8]}"
                camera_no = f"CAM_{project.id}_{cam_idx:02d}"
                camera_name = f"{project.name or '项目'}-{cam_idx}号布控球"

                # 生成经纬度（基于项目位置或默认值）
                base_lng = Decimal("118.796877") + Decimal(str(idx * 0.01))
                base_lat = Decimal("32.060255") + Decimal(str(cam_idx * 0.001))

                camera_device = DeviceResource(
                    id=camera_dev_id,
                    text=camera_name,
                    dev_short_name=f"{cam_idx}号",
                    dev_code=camera_no,
                    dev_type="10",  # 布控球
                    pid=proj_id,
                    path=f"/{root_id}/{proj_id}/{camera_dev_id}",
                    type=11,
                    is_group=0,
                    has_children=False,
                    status=1 if cam_idx % 2 == 1 else 0,  # 部分在线，部分离线
                    order=cam_idx,
                    is_available=1,
                    lng=base_lng,
                    lat=base_lat,
                    dvr_code=f"DVR_{uuid.uuid4().hex[:6]}",
                    gis_peer_code=f"GIS_{uuid.uuid4().hex[:6]}",
                    audio=1 if cam_idx % 2 == 1 else 0
                )
                db.add(camera_device)
                result["device_resources"] += 1

                # 生成camera表记录
                camera_id = f"CAM_{uuid.uuid4().hex[:8]}"
                camera = Camera(
                    id=camera_id,
                    camera_name=camera_name,
                    camera_no=camera_no,
                    province_code=project.location_province or "32",
                    creater_id="system",
                    create_time=datetime.now(),
                    updater_id="system",
                    update_time=datetime.now(),
                    delete_flag=0
                )
                db.add(camera)
                cameras_for_project.append(camera)
                result["cameras"] += 1

            # 更新项目节点的子节点数量
            project_node.children_count = camera_count

            # 4.3 生成站班会数据（每个项目1-2个站班会）
            talk_count = 1 if idx % 2 == 0 else 2
            for talk_idx in range(1, talk_count + 1):
                talk_id = f"TBT_{uuid.uuid4().hex[:8]}"

                # 确定工程类型
                project_type = 1  # 默认变电工程
                if project.single_project_type:
                    if "线路" in project.single_project_type:
                        project_type = 2
                    elif "电缆" in project.single_project_type:
                        project_type = 3

                # 生成站班会
                tool_box_talk = ToolBoxTalk(
                    id=talk_id,
                    off_online_flag=0,
                    prj_name=project.name or f"测试项目{idx}",
                    prj_code=project.prj_code or project.id,
                    ticket_id=f"TICKET_{uuid.uuid4().hex[:8]}",
                    ticket_no=f"GD-{project.id}-{talk_idx:03d}",
                    re_assessment_risk_level=talk_idx + 2,  # 风险等级3-4
                    current_constr_headcount=15 + talk_idx * 5,
                    construction_headcount=15 + talk_idx * 5,
                    work_start_time=datetime.now(),
                    current_constr_date=date.today(),
                    current_construction_status="01",  # 作业中
                    work_overnight_flag=0,
                    tool_box_talk_address=f"{project.location_municipality_name or '测试市'}{project.location_area_name or '测试区'}施工现场",
                    tool_box_talk_longitude=str(base_lng),
                    tool_box_talk_latitude=str(base_lat),
                    bidding_section_code=f"BD_{project.id}",
                    bidding_section_name=f"{project.name or '项目'}第一标段",
                    single_project_code=project.id,
                    single_project_name=project.name,
                    single_project_type=project_type,
                    constr_unified_social_credit_id=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
                    construction_unit_name=project.builder or "测试施工单位",
                    supervision_social_credit_code=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
                    supervision_unit_name=project.supervisor_organization or "测试监理单位",
                    voltage_level=project.voltage_level or "220KV",
                    huv_flag=1 if project.voltage_level and "500" in project.voltage_level else 0,
                    build_unit_code=project.build_unit_code or "BUILD_TEST",
                    province_code=project.location_province or "32",
                    creater_id="system",
                    create_time=datetime.now(),
                    updater_id="system",
                    update_time=datetime.now(),
                    delete_flag=0
                )
                db.add(tool_box_talk)
                result["tool_box_talks"] += 1

                # 4.4 关联站班会与布控球（每个站班会关联2-3个布控球）
                cameras_to_link = cameras_for_project[:min(2 + talk_idx, len(cameras_for_project))]
                for sort_no, camera in enumerate(cameras_to_link, start=1):
                    rela_id = f"RELA_{uuid.uuid4().hex[:8]}"
                    relation = ToolBoxTalkCameraRela(
                        id=rela_id,
                        camera_id=camera.id,
                        tool_box_talk_id=talk_id,
                        province_code=project.location_province or "32",
                        creater_id="system",
                        create_time=datetime.now(),
                        updater_id="system",
                        update_time=datetime.now(),
                        delete_flag=0,
                        sort_no=sort_no
                    )
                    db.add(relation)
                    result["relations"] += 1

            result["projects_used"].append({
                "id": project.id,
                "name": project.name,
                "voltage_level": project.voltage_level,
                "cameras": camera_count,
                "talks": talk_count
            })

        # 提交事务
        await db.commit()

        return result

    @staticmethod
    async def clear_test_data(db: AsyncSession) -> Dict[str, int]:
        """
        清空所有测试数据

        Returns:
            删除的记录数统计
        """
        from sqlalchemy import delete

        result = {
            "relations": 0,
            "cameras": 0,
            "tool_box_talks": 0,
            "device_resources": 0
        }

        # 按照外键依赖顺序删除
        # 1. 删除关联表
        rela_result = await db.execute(delete(ToolBoxTalkCameraRela))
        result["relations"] = rela_result.rowcount

        # 2. 删除camera
        camera_result = await db.execute(delete(Camera))
        result["cameras"] = camera_result.rowcount

        # 3. 删除站班会
        talk_result = await db.execute(delete(ToolBoxTalk))
        result["tool_box_talks"] = talk_result.rowcount

        # 4. 删除设备资源
        device_result = await db.execute(delete(DeviceResource))
        result["device_resources"] = device_result.rowcount

        await db.commit()

        return result
