# 测试数据生成系统 - 快速启动指南

## 已修复的问题

### 1. SQLAlchemy 类型注解错误
**问题：** 在 `Mapped[]` 中使用了 SQLAlchemy 类型而非 Python 类型

**修复文件：**
- ✅ `app/models/camera.py` - 修复类型注解 + 修复错误的 import
- ✅ `app/models/ps_single_project_info.py` - 修复类型注解
- ✅ `app/models/device_type.py` - 修复类型注解

**修复内容：**
```python
# 错误 ❌
from sqlalchemy.testing.schema import mapped_column  # 错误的导入
id: Mapped[String] = mapped_column(...)

# 正确 ✅
from sqlalchemy.orm import mapped_column
id: Mapped[str] = mapped_column(String(32), ...)
camera_name: Mapped[str | None] = mapped_column(String(64), nullable=True, ...)
```

### 2. 数据库表名错误
**问题：** `init.sql` 中表名包含中文字符

**修复：** `、toolboxtalk_camera_rela` → `toolboxtalk_camera_rela`

## 系统架构

```
接口层 (API)
    ↓
业务层 (Service)
    ↓
数据访问层 (DAO)
    ↓
数据模型层 (Model)
```

## 快速开始

### 方式1: 使用 FastAPI 接口（推荐）

```bash
# 1. 激活虚拟环境
source .venv/bin/activate

# 2. 启动服务
python app/main.py

# 3. 访问 Swagger 文档
open http://localhost:8000/docs

# 4. 在浏览器中调用接口
#    找到 "测试数据管理" -> "/test-data/generate"
#    点击 "Try it out" -> "Execute"
```

### 方式2: 使用测试脚本

```bash
# 激活虚拟环境
source .venv/bin/activate

# 运行测试脚本
python test_data_generation.py
```

### 方式3: 使用 curl 命令

```bash
# 生成测试数据（2个项目）
curl -X POST "http://localhost:8000/test-data/generate?project_limit=2"

# 查看数据状态
curl -X GET "http://localhost:8000/test-data/status"

# 清空测试数据
curl -X DELETE "http://localhost:8000/test-data/clear"
```

## API 接口说明

### 1. POST /test-data/generate

**功能：** 生成测试数据

**参数：**
- `project_limit` (可选): 使用的项目数量，默认2

**响应示例：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功生成测试数据：11个设备资源，6个布控球，3个站班会，7条关联关系",
  "resultValue": {
    "device_resources": 11,
    "cameras": 6,
    "tool_box_talks": 3,
    "relations": 7,
    "projects_used": [
      {
        "id": "项目ID",
        "name": "项目名称",
        "voltage_level": "220KV",
        "cameras": 3,
        "talks": 1
      }
    ]
  }
}
```

### 2. GET /test-data/status

**功能：** 查看当前数据状态

**响应示例：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "查询成功",
  "resultValue": {
    "device_resources": 11,
    "cameras": 6,
    "tool_box_talks": 3,
    "relations": 7
  }
}
```

### 3. DELETE /test-data/clear

**功能：** 清空所有测试数据

**警告：** ⚠️ 此操作不可恢复！

## 数据生成规则

### device_resource（设备资源树）
```
根节点
├── 项目1（从 ps_single_project_info 读取）
│   ├── 布控球设备1 (dev_type='10')
│   ├── 布控球设备2
│   └── 布控球设备3-5
└── 项目2
    └── 布控球设备...
```

### camera（布控球）
- `camera_no` = `device_resource.dev_code`
- `camera_name` = `device_resource.text`
- 每个项目生成 3-5 个布控球

### tool_box_talk（站班会）
- 项目信息来自 `ps_single_project_info`
- 每个项目生成 1-2 个站班会
- 风险等级: 3-4（中高风险）
- 作业状态: 01（作业中）

### toolboxtalk_camera_rela（关联关系）
- 每个站班会关联 2-3 个布控球
- `sort_no` 递增排序

## 前置条件

⚠️ **必须先导入 ps_single_project_info 表的真实数据**

如果没有数据，接口会返回错误：
```json
{
  "successful": false,
  "resultCode": 400,
  "resultHint": "未找到单项工程信息，请先导入ps_single_project_info数据"
}
```

## 数据库表关系

```
ps_single_project_info (真实项目数据)
         ↓
    [读取项目信息]
         ↓
device_resource (设备资源树)
         ↓
      camera (布控球)
         ↓
toolboxtalk_camera_rela (关联表)
         ↑
tool_box_talk (站班会)
```

## 文件清单

### Model 层
- ✅ `app/models/ps_single_project_info.py` - 单项工程信息
- ✅ `app/models/device_type.py` - 设备类型枚举
- ✅ `app/models/voltage_level.py` - 电压等级枚举
- ✅ `app/models/camera.py` - 布控球（已修复）
- ✅ `app/models/camera_rela.py` - 关联表
- ✅ `app/models/tool_box_talk.py` - 站班会
- ✅ `app/models/device_resource.py` - 设备资源

### DAO 层
- ✅ `app/dao/ps_single_project_info_dao.py`
- ✅ `app/dao/device_type_dao.py`
- ✅ `app/dao/voltage_level_dao.py`
- ✅ `app/dao/camera_dao.py`
- ✅ `app/dao/device_resource_dao.py`
- ✅ `app/dao/tool_box_talk_dao.py`
- ✅ `app/dao/toolboxtalk_camera_rela_dao.py`

### Service 层
- ✅ `app/services/test_data_service.py` - 测试数据生成服务

### API 层
- ✅ `app/api/test_data_api.py` - 测试数据管理接口

### 配置
- ✅ `app/core/routers.py` - 路由注册（已更新）

### 文档
- ✅ `docs/test_data_api.md` - API详细文档
- ✅ `README_QUICKSTART.md` - 本文件

### 测试
- ✅ `test_data_generation.py` - 测试脚本

## 故障排查

### 问题1: 模块导入错误
```
ModuleNotFoundError: No module named 'sqlalchemy'
```

**解决：** 激活虚拟环境
```bash
source .venv/bin/activate
```

### 问题2: 数据库连接失败
```
Connection refused
```

**解决：** 检查 `.env` 文件中的数据库配置
```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_DATABASE=uvp
```

### 问题3: 未找到项目数据
```
未找到单项工程信息，请先导入ps_single_project_info数据
```

**解决：** 先导入 `ps_single_project_info` 表的真实数据

## 下一步

1. ✅ 模型层已完成并修复
2. ✅ 数据访问层已完成
3. ✅ 业务逻辑层已完成
4. ✅ API接口层已完成
5. ⏳ **需要导入 ps_single_project_info 真实数据**
6. ⏳ 测试接口功能

## 联系支持

如有问题，请检查：
- `docs/test_data_api.md` - 详细API文档
- Swagger文档: `http://localhost:8000/docs`
- 项目日志: `logs/` 目录
