# UVP Backend

## 运行环境要求

- Python **3.10+（推荐 3.12）**
- MySQL **8.x**
- Redis **6.x+**

### 查看版本

```bash
python --version
pip --version

```

## 项目配置

### 创建 .env 文件

`cp .env.exmaple .env`

### 配置说明

#### MySQL

mysql+aiomysql://用户名:密码@IP:端口/数据库

⚠️ 必须使用 aiomysql，不能用 pymysql

#### Redis

无密码：

redis://127.0.0.1:6379/0

有密码：

redis://:password@127.0.0.1:6379/0

## 安装依赖

1. 创建虚拟环境（推荐）

`python -m venv .venv`

2. 激活虚拟环境

`source .venv/bin/activate`

Windows：

`.venv\Scripts\activate`

2. 安装依赖

`pip install -r requirements/dev.txt`

## 启动项目

`uvicorn app.main:app --reload`

或者 指定IP和端口号

`uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload`

启动成功会看到：

```text
INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000
```

## 访问地址

Swagger    http://127.0.0.1:8000/docs

OpenAPI    http://127.0.0.1:8000/openapi.json

Redoc    http://127.0.0.1:8000/redoc







