from fastapi import APIRouter, Depends

from app.core.security import auth_dependency

router = APIRouter(prefix="/uvp-backend-common/api/v1/tool-box-talk", tags=["站班会数据"],
                   dependencies=[Depends(auth_dependency)], )


@router.post("/mock", summary="生成站班会仿真数据",
             description="生成站班会仿真数据")
async def mock_tool_box_talk():
    return {"message": "站班会仿真数据生成成功"}


@router.post("/query", summary="查询站班会数据",
             description="根据条件查询站班会数据")
async def query_tool_box_talk():
    return {"data": []}
