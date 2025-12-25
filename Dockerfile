# ---------- builder ----------
FROM python:3.12-slim as builder

WORKDIR /app

# 系统依赖（mysql / redis client 常用）
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖定义
COPY requirements/ requirements/

# 安装 pip-tools
RUN pip install --no-cache-dir pip-tools

# 生成 lock 文件
RUN pip-complie requirements/base.in

# 安装依赖到虚拟路径
RUN pip install --no-cache-dir -r requirements/base.txt --prefix=/install

# ---------- runtime ----------
FROM python:3.12-slim

WORKDIR /app

# 拷贝依赖
COPY --from=builder /install /usr/local

# 拷贝代码
COPY app/ app/

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]