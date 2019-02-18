# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/2/18 下午4:45

from collections.abc import Mapping, MutableMapping

# dict属于mapping类型
a = {}
print(isinstance(a, MutableMapping))