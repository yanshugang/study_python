# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/12 下午2:51

"""
通过继承Thread来实现多线程
"""
import threading
import time


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    # 重写run方法
    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(4)
        print("get detail url end")


if __name__ == '__main__':
    t_1 = GetDetailHtml("get_detail_html")
    t_2 = GetDetailUrl("get_detail_url")

    start_time = time.time()

    t_1.start()
    t_2.start()

    t_1.join()
    t_2.join()

    print(time.time() - start_time)


