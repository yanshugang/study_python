import time


def gen_ab():
    print("start")
    yield "A"
    print("continue")
    yield "B"
    print("end")


for i in gen_ab():
    print(i)
    time.sleep(5)
