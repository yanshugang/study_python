"""
比较isinstance和type

推荐使用 isinstance
"""


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))  # True
print(isinstance(b, A))  # True

print(type(b) is B)  # True
print(type(b) is A)  # False
