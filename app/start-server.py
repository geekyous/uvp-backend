#!/usr/bin/env python3
"""
简单的 Web 服务器，用于测试页面
"""

import http.server
import socketserver
import os
import sys

def main():
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 设置端口
    port = 8080

    # 创建处理程序
    handler = http.server.SimpleHTTPRequestHandler

    # 允许列表目录
    handler.directory_listing = True

    print(f"启动 Web 服务器...")
    print(f"访问地址: http://localhost:{port}")
    print(f"服务器根目录: {current_dir}")
    print("\n按 Ctrl+C 停止服务器")

    try:
        # 创建服务器
        with socketserver.TCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        sys.exit(0)
    except Exception as e:
        print(f"启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()