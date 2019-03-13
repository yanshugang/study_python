# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午2:57


def t():
    t1 = "t1"

    def tt():
        a = "a"
        b = "b"
        c = "c"

        tt = vars()
        print(tt)

    print("haha")
    tt()


if __name__ == '__main__':
    t()
