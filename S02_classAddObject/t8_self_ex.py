# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午2:59
"""
python的自省机制
    自省：通过一定的机制查询到对象的内部结构
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))  # tuple可以直接解包
        return Date(int(year), int(month), int(day))  # 静态方法，此处使用硬编码，如果Date类名改了，此处也需要手动修改。

    # 类方法，直接传递class
    @classmethod
    def from_string(cls, data_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))  # 声明类方法，与静态方法相比，更加灵活

    # 判断传入的字符串是否合法
    @staticmethod
    def valid_str(data_str):
        year, month, day = tuple(data_str.split("-"))
        if int(year) > 0 and int(month) > 0 and int(month) <= 12 and int(day):
            return True

    # 定义__str__方法，可以实现当print时直接按规定格式打印
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,
                                             month=self.month,
                                             day=self.day)


class Person:
    """
    文档部分
    """
    name = "yanshugang"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == '__main__':
    user = Student("北京大学")

    # 通过__dict__查询属性
    print(user.__dict__)  # {'school_name': '北京大学'}
    print(user.name)  # yanshugang
    print(Person.__dict__)  # {'__module__': '__main__', '__doc__': '\n    文档部分\n    ', 'name': 'yanshugang', '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}

    user.__dict__["addr"] = "北京市"
    print(user.addr)

    print(dir(user))
