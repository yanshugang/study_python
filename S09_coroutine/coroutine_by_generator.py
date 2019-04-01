# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/1 下午3:22

"""
生成器实现协程
    1、用同步的方式编写异步的代码，在适当的时候暂停函数并在适当的时候启动函数；

生成器是可以暂停的函数，生成器是有状态的；
"""

import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from urllib.parse import urlparse

selector = DefaultSelector()


def get_socket_data():
    return "xxxxx"


def connected(self, key):
    selector.unregister(key.fd)  # 取消注册
    self.client.send(
        "GET {} HTTP/1.1 \r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf-8'))
    selector.register(self.client.fileno(), EVENT_READ, self.readable)


def downloader(url):
    url = urlparse(url)
    host = url.netloc

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    selector.register(client.fileno(), EVENT_WRITE, connected)
    source = yield from get_socket_data()

    data = source.decode("utf-8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)


def downlaod_html(url):
    html = yield from downloader(url)
    return html


if __name__ == '__main__':
    # 协程的调度依然是事件循环+协程模式，协程是单线程模式。
    url = "http://www.baidu.com"
    html = downlaod_html(url)
    next(html)
