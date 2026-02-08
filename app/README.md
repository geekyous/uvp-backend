# 测试数据管理页面

## 简介
这是一个简单的 Web 管理页面，用于：
- 查看测试数据状态
- 生成测试数据
- 清空测试数据

## 文件结构
```
web/
├── index.html    # 主页面
├── api.js        # JavaScript API 库
├── start-server.py  # Web 服务器启动脚本
└── README.md     # 说明文档
```

## 功能说明

### 🎯 核心功能
1. **数据状态查看** - 实时查看各表的数据统计
2. **生成测试数据** - 根据项目数量自动生成测试数据
3. **清空测试数据** - 清空所有测试数据（不可恢复）
4. **项目数量选择** - 可选择使用 1-10 个项目生成数据

### 📊 显示数据
- 设备资源总数
- 布控球数量
- 站班会数量
- 作业票数量
- 关联关系数量

### 🎨 交互特性
- 加载动画
- 操作确认
- 消息提示
- 自动刷新

## 使用方法

### 1. 启动后端服务
```bash
cd uvp-backend
source .venv/bin/activate
python app/main.py
```

### 2. 启动 Web 服务器（可选）
```bash
# 方法1：直接打开文件
open web/index.html

# 方法2：使用内置服务器
python web/start-server.py

# 方法3：使用 Python 简单服务器
cd web
python -m http.server 8080
# 然后访问 http://localhost:8080
```

### 3. 使用说明
1. 查看数据状态 - 点击"查看数据状态"按钮
2. 生成测试数据 - 选择项目数量，点击"生成测试数据"
3. 清空测试数据 - 两次确认后点击"清空测试数据"

## API 接口

页面调用的后端 API：

### GET /test-data/status
查询当前数据状态

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
    "construction_work_tickets": 3,
    "relations": 7
  }
}
```

### POST /test-data/generate?project_limit=2
生成测试数据

**参数：**
- `project_limit`: 使用的项目数量（默认2）

**响应示例：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功生成测试数据：11个设备资源，6个布控球，3个站班会，3个作业票，7条关联关系",
  "resultValue": {
    "device_resources": 11,
    "cameras": 6,
    "tool_box_talks": 3,
    "construction_work_tickets": 3,
    "relations": 7,
    "projects_used": [...]
  }
}
```

### DELETE /test-data/clear
清空测试数据

**响应示例：**
```json
{
  "successful": true,
  "resultCode": 200,
  "resultHint": "成功清空测试数据：删除7条关联，3个作业票，6个布控球，3个站班会，11个设备资源",
  "resultValue": {
    "relations": 7,
    "construction_work_tickets": 3,
    "cameras": 6,
    "tool_box_talks": 3,
    "device_resources": 11
  }
}
```

## 注意事项

1. **先导入 ps_single_project_info 数据**
   - 必须先导入单项工程信息表的真实数据
   - 否则生成测试数据会报错

2. **端口配置**
   - 默认端口：8000（后端）、8080（前端）
   - 请确保后端服务在 8000 端口运行
   - 可修改 `index.html` 中的 `API_BASE_URL` 配置

3. **浏览器兼容性**
   - 支持现代浏览器
   - Chrome、Firefox、Safari、Edge

4. **数据安全**
   - 清空操作不可恢复
   - 需要二次确认
   - 建议在测试环境使用

## 技术栈
- HTML5
- CSS3 (使用 Grid 布局)
- Vanilla JavaScript (ES6+)
- Fetch API
