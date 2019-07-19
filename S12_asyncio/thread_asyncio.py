"""
结合线程池和asyncio
在异步中使用多线程
在协程中集成阻塞io，把阻塞的代码放到线程池中去运行


一般不建议在协程中调用阻塞的方法，如果必须使用阻塞的方法，可以将阻塞放到线程池中运行。
"""

import asyncio
import socket
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor


# 阻塞接口
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
    print("===", data)

    client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)
    tasks = []
    for class_id in [100, 102, 103, 104, 105]:
        url = "https://coding.imooc.com/class/{}.html".format(class_id)
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
