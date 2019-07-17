# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/4/1 上午11:42

"""
委托生成器
子生成器

使用yield from 实现生成器嵌套

    1、调用方：调用委派生成器的客户端（调用方）代码
    2、委托生成器：包含yield from表达式的生成器函数
    3、子生成器：yield from后面加的生成器函数

委托生成器的作用是：在调用方与子生成器之间建立一个双向通道。

所谓的双向通道是什么意思呢？
调用方可以通过send()直接发送消息给子生成器，而子生成器yield的值，也是直接返回给调用方。



"""

final_result = {}


# 子生成器
def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield
        print(pro_name + "销量:", x)
        if not x:
            break
        total += x
        nums.append(x)

    return total, nums


# 委托生成器
def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！")


# 调用方
def main():
    data_sets = {
        "XX牌面膜": [1200, 1500, 3000],
        "XX牌手机": [28, 55, 98, 108],
        "XX牌大衣": [280, 560, 778, 70],
    }

    for key, data_set in data_sets.items():
        print("start key:", key)
        m = middle(key)  # 委托生成器
        m.send(None)  # 预激生成器

        for value in data_set:
            m.send(value)

        m.send(None)

    print("finale_result:", final_result)


def test_sales_sum():
    gen = sales_sum("xxx")
    gen.send(None)
    gen.send(1200)
    gen.send(1500)
    gen.send(3000)
    try:
        gen.send(None)
    except StopIteration as e:
        result = e.value
        print(result)


if __name__ == '__main__':
    main()
    # test_sales_sum()
