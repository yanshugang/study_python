"""
仅当for循环运行完毕时，运行else块
"""

my_list = []
for item in my_list:
    if item == "babab":
        break
else:
    raise ValueError("no babab")
