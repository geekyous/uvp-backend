from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import ApiResponse, success, fail
from app.services.test_data_service import TestDataService

router = APIRouter(prefix="/test-data", tags=["测试数据管理"])


@router.post("/generate", response_model=ApiResponse)
async def generate_test_data(
        project_limit: int = 2,
        db: AsyncSession = Depends(get_db)
) -> ApiResponse:
    """
    生成测试数据

    根据ps_single_project_info中的真实项目数据，生成测试用的：
    - device_resource（设备资源树）
    - camera（布控球）
    - tool_box_talk（站班会）
    - toolboxtalk_camera_rela（关联关系）

    Args:
        project_limit: 使用的项目数量（默认2个）
        db: 数据库会话

    Returns:
        生成结果统计
    """
    try:
        result = await TestDataService.generate_test_data(db, project_limit)
        return success(result_hint=f"成功生成测试数据：{result['device_resources']}个设备资源，"
                                   f"{result['cameras']}个布控球，{result['tool_box_talks']}个站班会，"
                                   f"{result['relations']}条关联关系")
    except ValueError as e:
        return fail(result_hint=str(e))
    except Exception as e:
        return fail(result_hint=f"生成测试数据失败：{str(e)}")


@router.delete("/clear", response_model=ApiResponse)
async def clear_test_data(
        db: AsyncSession = Depends(get_db)
) -> ApiResponse:
    """
    清空所有测试数据

    删除以下表的所有数据（按外键依赖顺序）：
    - toolboxtalk_camera_rela
    - camera
    - tool_box_talk
    - device_resource

    注意：此操作不可恢复，请谨慎使用！

    Returns:
        删除的记录数统计
    """
    try:
        result = await TestDataService.clear_test_data(db)
        return success(result_hint=f"成功清空测试数据：删除{result['relations']}条关联，"
                                   f"{result['cameras']}个布控球，{result['tool_box_talks']}个站班会，"
                                   f"{result['device_resources']}个设备资源")

    except Exception as e:
        return fail(result_hint=f"清空测试数据失败：{str(e)}")


@router.get("/status")
async def get_test_data_status(
        db: AsyncSession = Depends(get_db)
) -> ApiResponse:
    """
    查看当前测试数据状态

    Returns:
        各表的记录数统计
    """
    try:
        from sqlalchemy import select, func
        from app.models.device_resource import DeviceResource
        from app.models.camera import Camera
        from app.models.tool_box_talk import ToolBoxTalk
        from app.models.camera_rela import ToolBoxTalkCameraRela

        # 统计各表记录数
        device_count = await db.scalar(select(func.count(DeviceResource.id)))
        camera_count = await db.scalar(select(func.count(Camera.id)))
        talk_count = await db.scalar(select(func.count(ToolBoxTalk.id)))
        rela_count = await db.scalar(select(func.count(ToolBoxTalkCameraRela.id)))

        status = {
            "device_resources": device_count or 0,
            "cameras": camera_count or 0,
            "tool_box_talks": talk_count or 0,
            "relations": rela_count or 0
        }

        return success(result_hint="查询成功", data=status)
    except Exception as e:
        return fail(result_hint=f"查询状态失败：{str(e)}")
