"""
上下文管理器协议
通过__enter__和__exit__两个魔法方式实现；
"""


class Sample:
    def __enter__(self):
        print("enter")
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("exit")

    def do_something(self):
        print("doing something")


with Sample() as sample:
    # 执行函数前，解释器会自动先执行__enter__方法
    sample.do_something()
    # 执行完成后，解释器会自动执行__exit__方法
