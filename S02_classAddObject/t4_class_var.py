"""
类变量
"""


class A:
    # 类变量
    aa = 1

    def __init__(self, x, y):
        # 实例变量
        self.x = x
        self.y = y


a = A(2, 3)
print(a.x, a.y, a.aa)  # 实例中找不到aa时会向上查找类变量
print(A.aa)

A.aa = 100  # 修改类变量
a.aa = 111  # 新增实例变量

# 类变量是所有实例共享的
b = A(12, 13)
print(b.aa)
