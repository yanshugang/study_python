# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午3:01

"""
condition - 条件变量
    用于复杂的线程间同步

wait: 等待通知
notify: 通知
"""
import threading


class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 在！".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 好啊！".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 疑似地上霜！".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}: 小爱同学！".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 我们来对古诗吧！".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 窗前明月光！".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    cond = threading.Condition()

    # 启动顺序很重要。
    t_1 = XiaoAi(cond)
    t_2 = TianMao(cond)

    t_1.start()
    t_2.start()

# TODO：读源码
