# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午3:53
"""
semaphore: 用于控制进入数量的锁
    使用场景：
        文件的读写：一般只有一个写的线程，读允许有多个；
        爬虫：
"""

import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("get html text success")

        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider("http://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()

"""
Semaphore内部是使用Condition实现的。
"""
