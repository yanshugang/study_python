# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/8 下午3:35

"""
小工具：json文本转excel
"""
import json


def read_json(file):
    with open(file, "r") as fr:
        data = [json.loads(line) for line in fr.readlines()]
    return data


def write_excel():
    pass
