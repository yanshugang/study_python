"""
类和实例的属性

MRO算法：(Method Resolution Order)
    经典类：深度优先（DFS）[???]
    新式类：广度优先 [???]

    当前python3使用的C3算法。
"""


# 菱形继承关系
class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass


print(A.__mro__)


# 树状继承关系
class DD:
    pass


class EE:
    pass


class BB(DD):
    pass


class CC(EE):
    pass


class AA(BB, CC):
    pass


print(AA.__mro__)
