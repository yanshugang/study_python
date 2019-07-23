# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/14 下午4:41

"""
进程池
"""
import time
from multiprocessing import Pool, cpu_count


def get_html(n):
    time.sleep(n)
    print("sub_process success")
    return n


pool = Pool(cpu_count())
result = pool.apply_async(get_html, args=(3,))

# 关闭pool，不再接收任务
pool.close()
# 等待所有任务完成
pool.join()
print(result.get())

# imap: 按任务列表顺序
for result in pool.imap(get_html, [1, 5, 3]):
    print("{} sleep suuccess".format(result))

# imap_unordered: 按任务完成顺序
for result in pool.imap_unordered(get_html, [1, 5, 3]):
    print("{} sleep suuccess".format(result))
