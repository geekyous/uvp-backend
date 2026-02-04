#!/usr/bin/env python
"""
测试数据生成功能测试脚本
"""
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.core.config import settings
from app.services.test_data_service import TestDataService


async def test_service():
    """测试数据生成服务"""
    # 创建数据库引擎
    engine = create_async_engine(
        settings.SQLALCHEMY_DATABASE_URI,
        echo=True,
    )

    # 创建会话工厂
    SessionLocal = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with SessionLocal() as session:
        try:
            print("=" * 60)
            print("开始测试数据生成服务...")
            print("=" * 60)

            # 测试生成数据
            print("\n1. 生成测试数据（使用2个项目）...")
            result = await TestDataService.generate_test_data(session, project_limit=2)

            print(f"\n✓ 生成成功！")
            print(f"  - 设备资源: {result['device_resources']} 条")
            print(f"  - 布控球: {result['cameras']} 条")
            print(f"  - 站班会: {result['tool_box_talks']} 条")
            print(f"  - 关联关系: {result['relations']} 条")

            print("\n使用的项目:")
            for proj in result['projects_used']:
                print(f"  - {proj['name']} (ID: {proj['id']})")
                print(f"    电压等级: {proj['voltage_level']}")
                print(f"    布控球数: {proj['cameras']}")
                print(f"    站班会数: {proj['talks']}")

            print("\n" + "=" * 60)
            print("测试完成！")
            print("=" * 60)

        except Exception as e:
            print(f"\n✗ 测试失败: {str(e)}")
            import traceback
            traceback.print_exc()

    await engine.dispose()


if __name__ == "__main__":
    asyncio.run(test_service())
