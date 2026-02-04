# 测试数据生成接口使用说明

## 概述

本系统提供了基于真实项目数据自动生成测试数据的接口，用于业务测试。生成的数据包括：
- device_resource（设备资源树）
- camera（布控球）
- tool_box_talk（站班会）
- toolboxtalk_camera_rela（关联关系）

## 前置条件

**必须先导入 ps_single_project_info 表的真实数据**，否则无法生成测试数据。

数据库已包含以下基础数据：
- device_type（设备类型枚举）
- voltage_level（电压等级枚举）

## API 接口

### 1. 生成测试数据

```http
POST /test-data/generate?project_limit=2
```

**参数：**
- `project_limit`（可选）：使用的项目数量，默认2个

**功能：**
1. 从 ps_single_project_info 读取真实项目数据
2. 创建设备资源树（根节点 → 项目节点 → 布控球设备）
3. 生成对应的 camera 表记录
4. 生成站班会数据（每个项目1-2个站班会）
5. 建立站班会与布控球的关联关系

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
        "id": "proj_001",
        "name": "220kV变电站工程",
        "voltage_level": "220KV",
        "cameras": 3,
        "talks": 1
      }
    ]
  }
}
```

### 2. 查看数据状态

```http
GET /test-data/status
```

**功能：**
查看当前各表的记录数统计

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

### 3. 清空测试数据

```http
DELETE /test-data/clear
```

**功能：**
删除所有测试数据（按外键依赖顺序）

**警告：** 此操作不可恢复，请谨慎使用！

**响应示例：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功清空测试数据：删除7条关联，6个布控球，3个站班会，11个设备资源",
  "resultValue": {
    "relations": 7,
    "cameras": 6,
    "tool_box_talks": 3,
    "device_resources": 11
  }
}
```

## 数据生成规则

### device_resource（设备资源）

**树形结构：**
```
根节点（国网测试数据根节点）
├── 项目1节点
│   ├── 布控球1
│   ├── 布控球2
│   └── 布控球3
└── 项目2节点
    ├── 布控球1
    ├── 布控球2
    └── 布控球3
```

**字段映射：**
- `dev_type='00'`：根节点
- `dev_type='02'`：项目节点
- `dev_type='10'`：布控球设备（来自 device_type 表）
- `dev_code`：设备编码，格式 `CAM_{项目ID}_{序号}`
- `text`：设备名称
- `lng/lat`：经纬度坐标（自动生成）

### camera（布控球）

**数据对应：**
- `camera_no` = `device_resource.dev_code`
- `camera_name` = `device_resource.text`
- 每个项目生成 3-5 个布控球

### tool_box_talk（站班会）

**数据来源：**
- `prj_name`：来自 ps_single_project_info.name
- `prj_code`：来自 ps_single_project_info.prj_code
- `voltage_level`：来自 ps_single_project_info.voltage_level
- `construction_unit_name`：来自 ps_single_project_info.builder
- `supervision_unit_name`：来自 ps_single_project_info.supervisor_organization

**生成规则：**
- 每个项目生成 1-2 个站班会
- 风险等级：3-4（中高风险）
- 作业状态：01（作业中）
- 施工日期：当天

### toolboxtalk_camera_rela（关联关系）

**关联规则：**
- 每个站班会关联 2-3 个布控球
- `sort_no` 按顺序递增
- 来自同一项目的布控球

## 使用示例

### 场景1：初次生成测试数据

```bash
# 1. 先导入真实项目数据到 ps_single_project_info 表
# （通过数据导入脚本或工具）

# 2. 生成测试数据（使用2个项目）
curl -X POST "http://localhost:8000/test-data/generate?project_limit=2"

# 3. 查看生成结果
curl -X GET "http://localhost:8000/test-data/status"
```

### 场景2：重新生成测试数据

```bash
# 1. 清空现有测试数据
curl -X DELETE "http://localhost:8000/test-data/clear"

# 2. 重新生成（使用5个项目）
curl -X POST "http://localhost:8000/test-data/generate?project_limit=5"
```

### 场景3：通过 Swagger 文档操作

1. 访问 `http://localhost:8000/docs`
2. 找到 "测试数据管理" 标签
3. 使用可视化界面操作各个接口

## 注意事项

1. **必须先导入 ps_single_project_info 数据**，否则会报错
2. 生成的布控球编码格式：`CAM_{项目ID}_{序号}`
3. camera 表的 `camera_no` 字段有唯一约束，重复生成前需先清空
4. 清空操作会删除所有相关数据，请在开发/测试环境使用
5. 生产环境请勿使用清空接口

## 数据关系图

```
ps_single_project_info (真实数据)
         ↓
    [读取项目信息]
         ↓
    生成测试数据
         ↓
  ┌──────┴──────┐
  ↓             ↓
device_resource  tool_box_talk
  ↓             ↓
camera ←─── toolboxtalk_camera_rela
    (关联)
```

## 表关系说明

1. **device_resource ↔ camera**
   - camera.camera_no = device_resource.dev_code
   - camera.camera_name = device_resource.text

2. **tool_box_talk ↔ ps_single_project_info**
   - 站班会的项目信息来自单项工程信息表

3. **tool_box_talk ↔ camera**
   - 通过 toolboxtalk_camera_rela 中间表关联
   - 一对多关系（一个站班会可关联多个布控球）
