# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/21 下午3:02


from collections.abc import Iterable, Iterator

a = [1, 2]
iter_rator = iter(a)


# print(isinstance(a, Iterable))  # True  说明：list是可迭代对象
# print(isinstance(a, Iterator))  # False 说明：list不是迭代器
# print(isinstance(iter_rator, Iterable))  # True  说明：iter()函数可以将可迭代对象转换成迭代器
#
# print()
# print("=" * 20)


# 自己定义一个迭代器
class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑（迭代器不支持切片）
        try:
            value = self.iter_list[self.index]
        except IndexError:  # for语句只能处理StopIteration无法处理IndexError.
            raise StopIteration
        self.index += 1

        return value


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        """定义iter，一定要返回一个iterator，否则会异常"""
        return MyIterator(self.employee)

    def __getitem__(self, item):
        return self.employee[item]


if __name__ == '__main__':
    company = Company(["tom", "bob", "jane"])
    my_itor = iter(company)  # TODO: [重点] iter()函数首先会寻找是否有__iter__方法，如果有，直接调用；如果没有，则会创建一个默认的迭代器，调用__getitem__进行遍历。

    # next, 一直调用，知道抛出异常 StopIteration。
    while True:
        try:
            print(next(my_itor))
        except StopIteration:
            print("StopIteration")
            break

    # # TODO: for循环的内部实现机制
    # for item in company:
    #     print(item)
