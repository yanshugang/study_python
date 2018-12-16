"""
魔法方法: __add__\ __str__
"""


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_instance):
        re_vector = MyVector(self.x + other_instance.x, self.y + other_instance.y)
        return re_vector

    def __str__(self):
        return "x:{x}, y:{y}".format(x=self.x, y=self.y)


vec_1 = MyVector(1, 2)
vec_2 = MyVector(2, 3)
print(vec_1 + vec_2)
