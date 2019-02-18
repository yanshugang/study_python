# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午4:53

"""
dict常用操作
"""
# 创建空dict
a_1 = dict()
a_2 = {}

# clear: 清空
print("=" * 10, "clear", "=" * 10)
a = {"zhangsan": {"company": "baidu"}, "lisi": {"company": "alibaba"}}
a.clear()
print(a)

# copy: 返回浅拷贝。dict的copy是浅拷贝，即指向引用。修改一处便全部改变。
print("=" * 10, "copy", "=" * 10)
b = {"one": 1, "two": 2}
new_b = b.copy()
new_b["two"] = 222
print(b)  # {'one': 1, 'two': 2}
print(new_b)  # {'one': 1, 'two': 222}

# 深拷贝
print("=" * 10, "深拷贝", "=" * 10)
import copy

c = {"one": 1, "two": 2}
new_c = copy.deepcopy(c)
new_c["two"] = 222
print(c)
print(new_c)

# fromekeys
print("=" * 10, "fromekeys", "=" * 10)
d_list = ["aa", "bb"]
d_dict = dict.fromkeys(d_list, "default value")  # {'aa': 'default value', 'bb': 'default value'}
print(d_dict)

# get
e = {"one": 1, "two": 2}

try:
    e["three"]
except KeyError:
    print("KeyError")

e.get("three")  # 无返回值
e.get("three", 0)  # 返回指定默认值

# setdefault： D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D。
print("=" * 10, "setdefault", "=" * 10)
f = {"one": 1, "two": 2}
print(f.setdefault("two"))  # 2
print(f.setdefault("three", 222))  # 如果输入的key不存在，则返回默认值，并将该键值对添加到原字典中。
print(f)

# update: 合并dict
print("=" * 10, "update", "=" * 10)
g = {"one": 1, "two": 2}
g.update((("six", 6), ("seven", 7)))
print(g)

h = {"one": 1, "two": 2}
i = {"ten": 10}
h.update(i)
print(h)
