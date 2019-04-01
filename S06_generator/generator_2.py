"""
生成器高级
"""


def gen_func():
    html = yield "http://www.baidu.com"
    print("t", html)

    yield 2
    yield 3
    return "over"


if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)

    html = "haha"
    print(gen.send(html))
