"""
通过select实现http请求

1、epoll并不代表一定比select好
    在高并发的情况下，连接活跃度不是很高，epoll比select好
    在并发性不高，同时连接很活跃的情况下，select比epoll好
"""

# TODO: 没听懂，代码异常
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from urllib.parse import urlparse

selector = DefaultSelector()


class Fetcher:
    def connected(self, key):
        selector.unregister(key.fd)  # 取消注册
        self.client.send(
            "GET {} HTTP/1.1 \r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf-8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf-8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            print(e)

        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 事件循环，不停的请求socket的状态并调用对应的回调函数。
    # 1.select本身是不支持register模式。
    # 2.socket状态变化以后的回调是由程序员完成的
    while True:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)
            # 模式：回调+事件循环+select(poll/epoll)


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()
