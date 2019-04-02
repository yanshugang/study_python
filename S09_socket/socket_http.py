"""
使用socket实现http

request -> urllib -> socket
"""
import socket
from urllib.parse import urlparse


def get_url(url):
    # 通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path if url.path != "" else "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode('utf-8'))

    # 解决大于1k的数据
    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf-8")
    print(data)

    client.close()


if __name__ == '__main__':
    get_url("http://www.baidu.com")
