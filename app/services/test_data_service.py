import uuid
import random
from datetime import datetime, date, timedelta
from typing import Dict, Any, Tuple, Optional
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.dao.camera_dao import CameraDAO
from app.dao.construction_work_ticket_dao import ConstructionWorkTicketDAO
from app.dao.device_resource_dao import DeviceResourceDAO
from app.dao.device_type_dao import DeviceTypeDAO
from app.dao.ps_single_project_info_dao import PsSingleProjectInfoDAO
from app.dao.tool_box_talk_dao import ToolBoxTalkDAO
from app.dao.toolboxtalk_camera_rela_dao import ToolBoxTalkCameraRelaDAO
from app.models.camera import Camera
from app.models.camera_rela import ToolBoxTalkCameraRela
from app.models.construction_work_ticket import ConstructionWorkTicket
from app.models.device_resource import DeviceResource
from app.models.tool_box_talk import ToolBoxTalk
from app.services.test_data_reference import (
    CLASS_MEETING_REFERENCES,
    DATA_GENERATION_RULES,
    LOCATION_REFERENCES,
    format_ticket_no,
    generate_team_name,
    assign_risk_level,
    get_location_coords
)


class TestDataService:
    """测试数据生成服务"""

    # 默认坐标（安徽省合肥市）
    DEFAULT_LNG = 117.22
    DEFAULT_LAT = 31.82

    @staticmethod
    def _determine_project_type(project_type_str: Optional[str]) -> int:
        """
        根据项目类型字符串确定项目类型代码

        Args:
            project_type_str: 项目类型字符串

        Returns:
            项目类型代码（1=变电工程，2=线路工程，3=电缆工程）
        """
        if not project_type_str:
            return 1  # 默认变电工程
        if "线路" in project_type_str:
            return 2
        if "电缆" in project_type_str:
            return 3
        return 1

    @staticmethod
    def _normalize_voltage_level(voltage_level: Optional[str]) -> str:
        """
        标准化电压等级格式

        Args:
            voltage_level: 原始电压等级

        Returns:
            标准化后的电压等级
        """
        if not voltage_level:
            return "220kV"
        if "KV" in voltage_level and "750" not in voltage_level:
            return voltage_level.replace("KV", "kV")
        return voltage_level

    @staticmethod
    def _get_project_coords(
        project,
        offset_range: float = 0.01,
        debug_prefix: str = ""
    ) -> Tuple[Optional[Decimal], Optional[Decimal]]:
        """
        获取项目坐标，基于建设管理单位名称

        Args:
            project: 项目对象
            offset_range: 随机偏移范围（度）
            debug_prefix: 调试信息前缀

        Returns:
            (经度, 纬度) 元组
        """
        base_lng = None
        base_lat = None

        if project.build_unit_name:
            coords = get_location_coords(
                project.location_province or "",
                project.location_municipality_name or "",
                project.location_area_name or "",
                project.build_unit_name
            )
            if coords and coords[0] and coords[1]:
                lng_offset = random.uniform(-offset_range, offset_range)
                lat_offset = random.uniform(-offset_range, offset_range)
                base_lng = Decimal(str(float(coords[0]) + lng_offset))
                base_lat = Decimal(str(float(coords[1]) + lat_offset))
                print(f"DEBUG: {debug_prefix}使用 {project.build_unit_name} 坐标: {base_lng}, {base_lat}")
            else:
                print(f"DEBUG: {debug_prefix}未找到 {project.build_unit_name} 的坐标")
        else:
            print(f"DEBUG: {debug_prefix}build_unit_name 为空")

        # 使用默认坐标
        if base_lng is None or base_lat is None:
            base_lng = Decimal(str(TestDataService.DEFAULT_LNG + random.uniform(-offset_range, offset_range)))
            base_lat = Decimal(str(TestDataService.DEFAULT_LAT + random.uniform(-offset_range, offset_range)))
            print(f"DEBUG: {debug_prefix}使用默认坐标: {base_lng}, {base_lat}")

        return base_lng, base_lat

    @staticmethod
    def _get_camera_coords(
        project,
        offset_range: float = 0.01,
        camera_name: str = ""
    ) -> Tuple[Decimal, Decimal]:
        """
        获取布控球坐标

        Args:
            project: 项目对象
            offset_range: 随机偏移范围（度）
            camera_name: 布控球名称（用于调试信息）

        Returns:
            (经度, 纬度) 元组
        """
        base_lng = None
        base_lat = None

        if project.build_unit_name:
            coords = get_location_coords(
                project.location_province or "",
                project.location_municipality_name or "",
                project.location_area_name or "",
                project.build_unit_name
            )
            if coords and coords[0] and coords[1]:
                lng_offset = random.uniform(-offset_range, offset_range)
                lat_offset = random.uniform(-offset_range, offset_range)
                base_lng = Decimal(str(float(coords[0]) + lng_offset))
                base_lat = Decimal(str(float(coords[1]) + lat_offset))
                if camera_name:
                    print(f"DEBUG: 布控球 {camera_name} 使用 {project.build_unit_name} 坐标: {base_lng}, {base_lat}")
            else:
                base_lng = Decimal(str(TestDataService.DEFAULT_LNG + random.uniform(-offset_range, offset_range)))
                base_lat = Decimal(str(TestDataService.DEFAULT_LAT + random.uniform(-offset_range, offset_range)))
                if camera_name:
                    print(f"DEBUG: 布控球 {camera_name} 未找到 {project.build_unit_name} 的坐标，使用默认坐标: {base_lng}, {base_lat}")
        else:
            base_lng = Decimal(str(TestDataService.DEFAULT_LNG + random.uniform(-offset_range, offset_range)))
            base_lat = Decimal(str(TestDataService.DEFAULT_LAT + random.uniform(-offset_range, offset_range)))
            if camera_name:
                print(f"DEBUG: 布控球 {camera_name} 因 build_unit_name 为空使用默认坐标: {base_lng}, {base_lat}")

        return base_lng, base_lat

    @staticmethod
    def _create_root_node(projects_count: int) -> DeviceResource:
        """
        创建设备资源树的根节点

        Args:
            projects_count: 项目数量

        Returns:
            根节点设备资源对象
        """
        root_id = f"ROOT_{uuid.uuid4().hex[:8]}"
        return DeviceResource(
            id=root_id,
            text="国网江苏省电力公司",
            dev_code=f"ROOT_JIANGSU_{datetime.now().strftime('%Y%m%d')}",
            dev_type="00",
            pid=None,
            path=f"/{root_id}",
            type=0,
            is_group=1,
            has_children=True,
            status=1,
            children_count=projects_count,
            order=0,
            is_available=1
        )

    @staticmethod
    def _create_project_node(
        project,
        root_id: str,
        idx: int,
        lng: Optional[Decimal] = None,
        lat: Optional[Decimal] = None
    ) -> DeviceResource:
        """
        创建项目节点

        Args:
            project: 项目对象
            root_id: 根节点ID
            idx: 项目索引
            lng: 经度
            lat: 纬度

        Returns:
            项目节点设备资源对象
        """
        proj_id = f"PROJ_{uuid.uuid4().hex[:8]}"
        return DeviceResource(
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
            children_count=0,
            order=idx,
            is_available=1,
            lng=lng,
            lat=lat
        )

    @staticmethod
    def _create_camera_device(
        project,
        proj_id: str,
        root_id: str,
        cam_idx: int
    ) -> DeviceResource:
        """
        创建布控球设备资源

        Args:
            project: 项目对象
            proj_id: 项目节点ID
            root_id: 根节点ID
            cam_idx: 布控球索引

        Returns:
            布控球设备资源对象
        """
        camera_dev_id = f"DEV_{uuid.uuid4().hex[:8]}"
        camera_no = DATA_GENERATION_RULES["camera_code_format"].format(
            project_code=project.id,
            index=cam_idx
        )
        camera_name = f"{project.name or f'测试项目'}-{cam_idx}号布控球"

        base_lng, base_lat = TestDataService._get_camera_coords(project, 0.01, camera_name)

        return DeviceResource(
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
            status=1 if cam_idx % 2 == 1 else 0,
            order=cam_idx,
            is_available=1,
            lng=base_lng,
            lat=base_lat,
            dvr_code=f"DVR_{uuid.uuid4().hex[:6]}",
            gis_peer_code=f"GIS_{uuid.uuid4().hex[:6]}",
            audio=1 if cam_idx % 2 == 1 else 0
        )

    @staticmethod
    def _create_camera_record(
        project,
        cam_idx: int,
        camera_name: str,
        camera_no: str
    ) -> Camera:
        """
        创建布控球记录

        Args:
            project: 项目对象
            cam_idx: 布控球索引
            camera_name: 布控球名称
            camera_no: 布控球编号

        Returns:
            布控球记录对象
        """
        camera_id = f"CAM_{uuid.uuid4().hex[:8]}"
        return Camera(
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

    @staticmethod
    def _create_tool_box_talk(
        project,
        idx: int,
        talk_idx: int,
        ticket_id: str,
        ticket_no: str,
        risk_level: str,
        worker_count: int,
        project_type: int,
        voltage_level: str,
        base_lng: Optional[Decimal] = None,
        base_lat: Optional[Decimal] = None
    ) -> ToolBoxTalk:
        """
        创建站班会记录

        Args:
            project: 项目对象
            idx: 项目索引
            talk_idx: 站班会索引
            ticket_id: 作业票ID
            ticket_no: 作业票编号
            risk_level: 风险等级
            worker_count: 施工人数
            project_type: 项目类型
            voltage_level: 电压等级
            base_lng: 经度
            base_lat: 纬度

        Returns:
            站班会记录对象
        """
        talk_id = f"TBT_{uuid.uuid4().hex[:8]}"
        team_id = f"TEAM_{uuid.uuid4().hex[:8]}"
        team_name = generate_team_name(talk_idx, str(project_type))

        return ToolBoxTalk(
            id=talk_id,
            off_online_flag=0,
            prj_name=project.name or f"测试项目{idx}",
            prj_code=project.prj_code or project.id,
            ticket_id=ticket_id,
            ticket_no=ticket_no,
            re_assessment_risk_level=risk_level,
            current_constr_headcount=worker_count,
            construction_headcount=worker_count,
            work_start_time=datetime.now(),
            current_constr_date=date.today(),
            current_construction_status="01",
            work_overnight_flag=0,
            tool_box_talk_address=f"{project.location_municipality_name or '测试市'}{project.location_area_name or '测试区'}施工现场",
            tool_box_talk_longitude=str(base_lng) if base_lng else "",
            tool_box_talk_latitude=str(base_lat) if base_lat else "",
            bidding_section_code=f"BD_{project.id}",
            bidding_section_name=f"{project.name or f'测试项目{idx}'}第一标段",
            single_project_code=project.id,
            single_project_name=project.name,
            single_project_type=project_type,
            constr_unified_social_credit_id=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
            construction_unit_name=project.build_unit_name or "测试施工单位",
            supervision_social_credit_code=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
            supervision_unit_name=project.supervisor_organization or "测试监理单位",
            voltage_level=voltage_level,
            huv_flag=0,
            build_unit_code=project.build_unit_code or "BUILD_TEST",
            province_code=project.location_province or "32",
            creater_id="system",
            create_time=datetime.now(),
            updater_id="system",
            update_time=datetime.now(),
            delete_flag=0
        )

    @staticmethod
    def _create_construction_work_ticket(
        project,
        idx: int,
        talk_idx: int,
        ticket_id: str,
        ticket_no: str,
        risk_level: str,
        worker_count: int,
        project_type: int,
        voltage_level: str,
        team_name: str
    ) -> ConstructionWorkTicket:
        """
        创建作业票记录

        Args:
            project: 项目对象
            idx: 项目索引
            talk_idx: 站班会索引
            ticket_id: 作业票ID
            ticket_no: 作业票编号
            risk_level: 风险等级
            worker_count: 施工人数
            project_type: 项目类型
            voltage_level: 电压等级
            team_name: 班组名称

        Returns:
            作业票记录对象
        """
        team_id = f"TEAM_{uuid.uuid4().hex[:8]}"
        start_offset = DATA_GENERATION_RULES["planned_days_offset"]["start"]
        end_offset = DATA_GENERATION_RULES["planned_days_offset"]["end"]

        return ConstructionWorkTicket(
            id=ticket_id,
            ticket_type="A" if talk_idx % 2 == 0 else "B",
            ticket_no=ticket_no,
            ticket_name=f"{project.name or f'测试项目{idx}'}-施工作业票{talk_idx}",
            bidding_section_code=f"BD_{project.id}",
            bidding_section_name=f"{project.name or f'测试项目{idx}'}第一标段",
            single_project_type=project_type,
            single_project_code=project.id,
            single_project_name=project.name,
            team_id=team_id,
            working_team_name=team_name,
            construction_headcount=worker_count,
            planned_start_date=datetime.now() - timedelta(days=start_offset),
            planned_end_date=datetime.now() + timedelta(days=end_offset),
            start_time=datetime.now(),
            end_time=datetime.now() + timedelta(hours=DATA_GENERATION_RULES["working_hours"]["default"]),
            assessment_risk_level=risk_level,
            re_assessment_risk_level=risk_level,
            ticket_status="05",
            current_construction_status="01",
            audit_hierarchy="03",
            issue_type="02",
            issue_date=datetime.now(),
            priority="01" if talk_idx == 1 else "02",
            build_unit_code=project.build_unit_code or "BUILD_TEST",
            province_code=project.location_province or "32",
            remark=f"测试作业票-{talk_idx}",
            huv_flag=0,
            voltage_level=voltage_level,
            construction_unit_name=project.build_unit_name or "测试施工单位",
            construction_social_credit_code=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
            supervision_unit_name=project.supervisor_organization or "测试监理单位",
            supervision_social_credit_code=f"91{project.location_province or '32'}00MA{uuid.uuid4().hex[:8].upper()}",
            creater_id="system",
            create_time=datetime.now(),
            updater_id="system",
            update_time=datetime.now(),
            delete_flag=0
        )

    @staticmethod
    def _create_camera_relations(
        db: AsyncSession,
        cameras: list,
        talk_id: str,
        project
    ) -> int:
        """
        创建布控球与站班会的关联关系

        Args:
            db: 数据库会话
            cameras: 布控球列表
            talk_id: 站班会ID
            project: 项目对象

        Returns:
            创建的关联关系数量
        """
        relation_count = 0
        cameras_to_link = cameras[:min(DATA_GENERATION_RULES["cameras_per_talk"]["max"], len(cameras))]

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
            relation_count += 1

        return relation_count

    @staticmethod
    async def _validate_prerequisites(db: AsyncSession, project_limit: int) -> Tuple[list, Any]:
        """
        验证生成数据的前置条件

        Args:
            db: 数据库会话
            project_limit: 项目数量限制

        Returns:
            (项目列表, 设备类型对象) 元组

        Raises:
            ValueError: 如果前置条件不满足
        """
        projects = await PsSingleProjectInfoDAO.list_all(db, limit=project_limit)
        if not projects:
            raise ValueError("未找到单项工程信息，请先导入ps_single_project_info数据")

        device_type = await DeviceTypeDAO.get_by_code(db, "10")  # 布控球
        if not device_type:
            raise ValueError("未找到布控球设备类型（type_code=10）")

        return projects, device_type

    @staticmethod
    async def generate_test_data(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        生成测试数据（参考实际业务数据）

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
            "construction_work_tickets": 0,
            "relations": 0,
            "projects_used": []
        }

        # 验证前置条件
        projects, device_type = await TestDataService._validate_prerequisites(db, project_limit)

        # 创建根节点
        root = TestDataService._create_root_node(len(projects))
        db.add(root)
        result["device_resources"] += 1
        root_id = root.id

        # 为每个项目生成数据
        for idx, project in enumerate(projects, start=1):
            # 确定项目类型和电压等级
            project_type = TestDataService._determine_project_type(project.single_project_type)
            voltage_level = TestDataService._normalize_voltage_level(project.voltage_level)

            # 创建项目节点
            project_node = TestDataService._create_project_node(project, root_id, idx)
            db.add(project_node)
            result["device_resources"] += 1
            proj_id = project_node.id

            # 生成布控球设备
            camera_count = DATA_GENERATION_RULES["cameras_per_project"]["min"]
            cameras_for_project = []

            for cam_idx in range(1, camera_count + 1):
                # 创建设备资源中的布控球
                camera_device = TestDataService._create_camera_device(project, proj_id, root_id, cam_idx)
                db.add(camera_device)
                result["device_resources"] += 1

                # 创建camera表记录
                camera = TestDataService._create_camera_record(
                    project, cam_idx, camera_device.text, camera_device.dev_code
                )
                db.add(camera)
                cameras_for_project.append(camera)
                result["cameras"] += 1

            # 更新项目节点的子节点数量
            project_node.children_count = camera_count

            # 获取项目坐标用于站班会
            base_lng, base_lat = TestDataService._get_project_coords(project, debug_prefix=f"项目 {project.name} ")

            # 生成站班会数据
            talk_count = 1 if idx % 2 == 0 else 2
            for talk_idx in range(1, talk_count + 1):
                # 生成票号和票ID
                ticket_id = f"TICKET_{uuid.uuid4().hex[:8]}"
                ticket_no = format_ticket_no(project.prj_code or project.id, talk_idx)

                # 确定施工人数和风险等级
                worker_count = DATA_GENERATION_RULES["worker_count_ranges"][talk_idx % 3]
                risk_level = assign_risk_level(worker_count, 0)

                # 生成站班会
                tool_box_talk = TestDataService._create_tool_box_talk(
                    project, idx, talk_idx, ticket_id, ticket_no, risk_level,
                    worker_count, project_type, voltage_level, base_lng, base_lat
                )
                db.add(tool_box_talk)
                result["tool_box_talks"] += 1

                # 生成作业票
                team_name = generate_team_name(talk_idx, str(project_type))
                work_ticket = TestDataService._create_construction_work_ticket(
                    project, idx, talk_idx, ticket_id, ticket_no, risk_level,
                    worker_count, project_type, voltage_level, team_name
                )
                db.add(work_ticket)
                result["construction_work_tickets"] += 1

                # 关联站班会与布控球
                relation_count = TestDataService._create_camera_relations(
                    db, cameras_for_project, tool_box_talk.id, project
                )
                result["relations"] += relation_count

            # 记录项目信息
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
    async def generate_device_resources(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        只生成设备资源树

        Args:
            db: 数据库会话
            project_limit: 使用的项目数量限制

        Returns:
            生成结果统计
        """
        result = {"device_resources": 0}

        # 获取真实项目数据
        projects = await PsSingleProjectInfoDAO.list_all(db, limit=project_limit)
        if not projects:
            raise ValueError("未找到单项工程信息，请先导入ps_single_project_info数据")

        # 创建根节点
        root = TestDataService._create_root_node(len(projects))
        db.add(root)
        result["device_resources"] += 1
        root_id = root.id

        # 为每个项目生成数据
        for idx, project in enumerate(projects, start=1):
            # 获取项目坐标
            project_lng, project_lat = TestDataService._get_project_coords(
                project, offset_range=0.005, debug_prefix=f"项目 {project.name} "
            )

            # 创建项目节点
            project_node = TestDataService._create_project_node(project, root_id, idx, project_lng, project_lat)
            db.add(project_node)
            result["device_resources"] += 1

        await db.commit()

        return result

    @staticmethod
    async def generate_cameras(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        只生成布控球（设备）

        Args:
            db: 数据库会话
            project_limit: 使用的项目数量限制

        Returns:
            生成结果统计
        """
        result = {
            "cameras": 0,
            "device_resources": 0
        }

        # 验证前置条件
        projects, device_type = await TestDataService._validate_prerequisites(db, project_limit)

        # 为每个项目生成布控球设备
        for idx, project in enumerate(projects, start=1):
            camera_count = DATA_GENERATION_RULES["cameras_per_project"]["min"]
            proj_id = f"PROJ_{project.id}"
            root_id = "ROOT_JIANGSU"

            for cam_idx in range(1, camera_count + 1):
                # 创建设备资源中的布控球
                camera_device = TestDataService._create_camera_device(project, proj_id, root_id, cam_idx)
                camera_device.path = f"/ROOT_JIANGSU/{project.id}/{camera_device.id}"  # 更新路径
                db.add(camera_device)
                result["device_resources"] += 1

                # 创建camera表记录
                camera = TestDataService._create_camera_record(
                    project, cam_idx, camera_device.text, camera_device.dev_code
                )
                db.add(camera)
                result["cameras"] += 1

        await db.commit()

        return result

    @staticmethod
    async def generate_tool_box_talks(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        只生成站班会

        Args:
            db: 数据库会话
            project_limit: 使用的项目数量限制

        Returns:
            生成结果统计
        """
        result = {
            "tool_box_talks": 0,
            "construction_work_tickets": 0,
            "device_resources": 0
        }

        # 获取真实项目数据
        projects = await PsSingleProjectInfoDAO.list_all(db, limit=project_limit)
        if not projects:
            raise ValueError("未找到单项工程信息，请先导入ps_single_project_info数据")

        # 为每个项目生成站班会数据
        for idx, project in enumerate(projects, start=1):
            # 确定项目类型和电压等级
            project_type = TestDataService._determine_project_type(project.single_project_type)
            voltage_level = TestDataService._normalize_voltage_level(project.voltage_level)

            # 获取项目坐标
            base_lng = None
            base_lat = None
            if project.build_unit_name:
                coords = get_location_coords(
                    project.location_province or "",
                    project.location_municipality_name or "",
                    project.location_area_name or "",
                    project.build_unit_name
                )
                if coords and coords[0] and coords[1]:
                    base_lng = coords[0]
                    base_lat = coords[1]

            # 生成站班会数据
            talk_count = 1 if idx % 2 == 0 else 2
            for talk_idx in range(1, talk_count + 1):
                # 生成票号和票ID
                ticket_id = f"TICKET_{uuid.uuid4().hex[:8]}"
                ticket_no = format_ticket_no(project.prj_code or project.id, talk_idx)

                # 确定施工人数和风险等级
                worker_count = DATA_GENERATION_RULES["worker_count_ranges"][talk_idx % 3]
                risk_level = assign_risk_level(worker_count, 0)

                # 生成站班会
                tool_box_talk = TestDataService._create_tool_box_talk(
                    project, idx, talk_idx, ticket_id, ticket_no, risk_level,
                    worker_count, project_type, voltage_level, base_lng, base_lat
                )
                db.add(tool_box_talk)
                result["tool_box_talks"] += 1

                # 生成作业票
                team_name = generate_team_name(talk_idx, str(project_type))
                work_ticket = TestDataService._create_construction_work_ticket(
                    project, idx, talk_idx, ticket_id, ticket_no, risk_level,
                    worker_count, project_type, voltage_level, team_name
                )
                db.add(work_ticket)
                result["construction_work_tickets"] += 1

        await db.commit()

        return result

    @staticmethod
    async def generate_relations(db: AsyncSession, project_limit: int = 2) -> Dict[str, Any]:
        """
        生成关联关系（站班会与布控球的关联）

        Args:
            db: 数据库会话
            project_limit: 使用的项目数量限制

        Returns:
            生成结果统计
        """
        result = {
            "relations": 0,
            "device_resources": 0
        }

        # 获取真实项目数据
        projects = await PsSingleProjectInfoDAO.list_all(db, limit=project_limit)
        if not projects:
            raise ValueError("未找到单项工程信息，请先导入ps_single_project_info数据")

        # 为每个项目生成关联关系
        for idx, project in enumerate(projects, start=1):
            # 查找该项目的所有布控球
            cameras = await CameraDAO.list_by_project(db, project.id)
            if not cameras:
                print(f"警告：项目 {project.id} 没有找到布控球，跳过关联关系生成")
                continue

            # 查找该项目的所有站班会
            talks = await ToolBoxTalkDAO.list_by_project(db, project.prj_code if project.prj_code else project.id)
            if not talks:
                print(f"警告：项目 {project.id} 没有找到站班会，跳过关联关系生成")
                continue

            # 为每个站班会关联布控球
            for talk in talks:
                relation_count = TestDataService._create_camera_relations(db, cameras, talk.id, project)
                result["relations"] += relation_count

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
            "construction_work_tickets": 0,
            "device_resources": 0
        }

        # 按照外键依赖顺序删除
        rela_result = await db.execute(delete(ToolBoxTalkCameraRela))
        result["relations"] = rela_result.rowcount

        ticket_result = await db.execute(delete(ConstructionWorkTicket))
        result["construction_work_tickets"] = ticket_result.rowcount

        camera_result = await db.execute(delete(Camera))
        result["cameras"] = camera_result.rowcount

        talk_result = await db.execute(delete(ToolBoxTalk))
        result["tool_box_talks"] = talk_result.rowcount

        device_result = await db.execute(delete(DeviceResource))
        result["device_resources"] = device_result.rowcount

        await db.commit()

        return result
