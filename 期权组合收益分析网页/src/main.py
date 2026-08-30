import http.server
import socketserver
import os

PORT = 8080

# 设置服务目录为 src 文件夹
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f'服务器运行在 http://localhost:{PORT}')
    print(f'服务目录: {os.getcwd()}')
    httpd.serve_forever()
