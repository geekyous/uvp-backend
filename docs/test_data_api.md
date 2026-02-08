# 测试数据生成接口使用说明

## 概述

本系统提供了**基于实际业务数据**自动生成测试数据的接口，数据生成时会参考真实的业务数据格式和内容。

生成的数据包括：
- device_resource（设备资源树）
- camera（布控球）
- tool_box_talk（站班会）
- construction_work_ticket（施工作业票）- **新增**
- toolboxtalk_camera_rela（关联关系）

## 前置条件

**必须先导入 ps_single_project_info 表的真实数据**，否则无法生成测试数据。

数据库已包含以下基础数据：
- device_type（设备类型枚举）
- voltage_level（电压等级枚举）

## 数据生成规则

### 项目数据来源

测试数据生成会从 `ps_single_project_info` 表读取真实项目数据，并根据这些项目生成对应的测试数据。

### 参考数据结构

系统内置了参考数据配置（`test_data_reference.py`），包含：

1. **项目参考数据**
   - 3个示例项目（埇桥、刘尧、苏州项目）
   - 包含电压等级、工程类型、地理位置等信息
   - 建设管理单位信息（build_unit_code、build_unit_name等）

2. **作业票参考数据**
   - 票班与作业票一对一关联
   - 作业票类型：A票、B票
   - 风险等级：根据施工人数动态分配
   - 审批层级、优先级等

3. **设备资源参考数据**
   - 设备类型：布控球（dev_type='10'）
   - 布控球命名格式：工程名称-序号号布控球

### 4. 数据生成规则

- 施工人数范围：[14, 15, 18, 20, 25, 30] 人
- 布控球数量：每项目3-8个
- 站班会数量：每项目1-2个
- 作业票数量：每站班会对应1个作业票
- 布控球关联：每站班会关联2-5个布控球

## API 接口

### 1. 生成测试数据

```http
POST /test-data/generate?project_limit=2
```

**参数：**
- `project_limit`（可选）：使用的项目数量，默认2个

**功能：**
1. 从 `ps_single_project_info` 读取真实项目数据
2. 创建设备资源树（根节点 → 项目节点 → 布控球设备）
3. 生成对应的 camera 表记录
4. 生成站班会数据
5. 生成作业票数据（与站班会关联）
6. 建立站班会与布控球的关联关系

**返回数据：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功生成测试数据：XX个设备资源，XX个布控球，XX个站班会，XX个作业票，XX条关联关系",
  "resultValue": {
    "device_resources": XX,
    "cameras": XX,
    "tool_box_talks": XX,
    "construction_work_tickets": XX,
    "relations": XX,
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

### 2. 查看数据状态

```http
GET /test-data/status
```

**功能：** 查看当前各表的记录数统计

**返回数据：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "查询成功",
  "resultValue": {
    "device_resources": 11,
    "cameras": 6,
    "tool_box_talks": 3,
    "construction_work_tickets": 3,
    "relations": 7
  }
}
```

### 3. 清空测试数据

```http
DELETE /test-data/clear
```

**功能：** 删除以下表的所有数据（按外键依赖顺序）：
1. toolboxtalk_camera_rela
2. construction_work_ticket
3. camera
4. tool_box_talk
5. device_resource

**警告：** ⚠️ 此操作不可恢复，请谨慎使用！

**返回数据：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功清空测试数据：删除XX条关联，XX个作业票，XX个布控球，XX个站班会，XX个设备资源",
  "resultValue": {
    "relations": XX,
    "construction_work_tickets": XX,
    "cameras": XX,
    "tool_box_talks": XX,
    "device_resources": XX
  }
}
```

## 数据生成详细说明

### device_resource（设备资源树）

```
根节点（国网江苏省电力公司）
├── 项目1（从 ps_single_project_info 读取）
│   ├── 布控球设备1 (dev_type='10')
│   ├── 布控球设备2
│   └── 布控球设备3-5
└── 项目2
    ├── 布控球设备1
    └── 布控球设备2-3
```

**特点：**
- 设备类型：布控球（dev_type='10'）
- 部分设备在线（status=1），部分离线（status=0）
- 每个项目生成3-8个布控球（根据项目序号）
- 布控球命名："{项目名称}-{序号}号布控球"
- 经纬度：根据项目省份和市区自动生成

### camera（布控球）

- `camera_no` = `device_resource.dev_code`
- `camera_name` = `device_resource.text`
- `province_code` = 从 `ps_single_project_info.location_province` 获取

### tool_box_talk（站班会）

**项目信息来源：** 从 ps_single_project_info 获取

| 字段 | 数据来源 |
|------|---------|
| prj_name | ps_single_project_info.name |
| prj_code | ps_single_project_info.prj_code |
| build_unit_code | ps_single_project_info.build_unit_code |
| build_unit_name | ps_single_project_info.build_unit_name |
| construction_unit_name | ps_single_project_info.builder |
| supervision_unit_name | ps_single_project_info.supervisor_organization |
| voltage_level | ps_single_project_info.voltage_level |
| huv_flag | 根据 voltage_level 判断（500kV及以上为特高压） |
| province_code | ps_single_project_info.location_province |

**业务规则：**
- 风险等级：根据施工人数动态分配
  - < 10人：2（低风险）
  - 10-20人：3（中风险）
  - 20-30人：4（高风险）
  - > 30人：5（特高风险）
- 施工人数：[14, 15, 18, 20, 25, 30] 人
- 施工日期：当天
- 施工状态：01（作业中）
- 工程类型：根据项目名称判断
  - "线路工程" → type=2
  - "电缆工程" → type=3
  - 默认 → type=1（变电工程）
- 作业票编号："{项目编码}-{站班会序号:03d}"
- 站班会地址："{市}{区}施工现场"

### construction_work_ticket（施工作业票）- 新增

**关联关系：** 与 tool_box_talk 一一对应

**业务规则：**
- 作业票类型：A票或B票（根据站班会索引决定）
- 班组名称：自动生成（线路组塔架线-XX班、变电站XX班等）
- 施工人数：与站班会的当日作业人数相同
- 风险等级：与站班会的风险等级相同
- 作业票状态：05（执行中）
- 审批层级：03（监理）
- 签发类型：02（自动签发）
- 优先级：高（01）或中（02）
- 计划时间：自动计算（当前时间 ± 偏移天数）
- 施工时间：根据工作时长自动计算（8、10小时等）
- 建设管理单位：从 ps_single_project_info 获取
  - build_unit_code
  - build_unit_name
  - construction_unit_name
  - supervision_unit_name
  - 相关信用代码：自动生成格式"91{省份}00MA{UUID}.upper()"

### toolboxtalk_camera_rela（关联关系）

- 一个站班会关联 2-5 个布控球
- sort_no 递增排序
- 从同一项目的布控球中选择

## 使用示例

### 场景1：初次生成测试数据

```bash
# 1. 先导入 ps_single_project_info 真实数据
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

# 3. 查看新数据状态
curl -X GET "http://localhost:8000/test-data/status"
```

### 场景3：通过 Swagger 文档操作

1. 访问 `http://localhost:8000/docs`
2. 找到 "测试数据管理" 标签
3. 点击 "Try it out" 执行接口

## 参考数据字段映射

### ps_single_project_info → tool_box_talk

| tool_box_talk 字段 | ps_single_project_info 字段 |
|-------------------|------------------------|
| prj_name | name |
| prj_code | prj_code |
| build_unit_code | build_unit_code |
| build_unit_name | build_unit_name |
| construction_unit_name | builder |
| supervision_unit_name | supervisor_organization |
| voltage_level | voltage_level |
| province_code | location_province |

### ps_single_project_info → construction_work_ticket

| construction_work_ticket 字段 | ps_single_project_info 字段 |
|--------------------------|-------------------|
| single_project_code | id |
| single_project_name | name |
| bidding_section_code | 自动生成（BD_{id}） |
| bidding_section_name | 自动生成（{name}第一标段） |
| build_unit_code | build_unit_code |
| build_unit_name | build_unit_name |
| construction_unit_name | builder |
| supervision_unit_name | supervisor_organization |
| voltage_level | voltage_level |
| province_code | location_province |

## 注意事项

### 1. **必须先导入 ps_single_project_info 数据**

如果没有项目数据，调用接口会报错：
```
未找到单项工程信息，请先导入ps_single_project_info数据
```

### 2. **数据关系**

- `tool_box_talk.ticket_id` 与 `construction_work_ticket.id` 一一对应
- `tool_box_talk.ticket_no` 与 `construction_work_ticket.ticket_no` 一一对应
- 确保数据一致性

### 3. **事务处理**

测试数据生成在一个事务中完成，如果任何步骤失败，整个事务会回滚，不会产生脏数据。

### 4. **清空操作**

清空数据时按照外键依赖顺序删除：
1. toolboxtalk_camera_rela
2. construction_work_ticket
3. camera
4. tool_box_talk
5. device_resource

清空操作不可恢复，请谨慎使用！

## 文件清单

- ✅ `app/models/construction_work_ticket.py` - 作业票模型
- ✅ `app/dao/construction_work_ticket_dao.py` - 作业票DAO（16个方法）
- ✅ `app/services/test_data_reference.py` - 参考数据配置（新增）
- ✅ `app/services/test_data_service.py` - 测试数据服务（已更新）
- ✅ `app/api/test_data_api.py` - 测试数据API（已更新）
- ✅ `docs/test_data_api.md` - 本文档

## 文件清单

| 类别 | 数量 | 说明 |
|------|------|------|
| Model文件 | 10个 | 新增1个作业票模型 |
| DAO文件 | 10个 | 新增1个作业票DAO |
| DAO方法 | 94个 | 新增16个作业票方法 |
| Service文件 | 7个 | 更新测试数据服务 |
| API接口 | 16个 | 更新3个接口文档 |

## 快速开始

```bash
# 启动服务
source .venv/bin/activate
python app/main.py

# 访问接口文档
open http://localhost:8000/docs

# 测试接口（需要先导入ps_single_project_info数据）
curl -X POST "http://localhost:8000/test-data/generate?project_limit=2"
```
