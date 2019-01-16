import contextlib


# 把一个函数变成一个上下文管理器, 这个函数必须是生成器
@contextlib.contextmanager
def file_open(file_name):
    print("like enter: file open")
    yield {}
    print("like exit: file end")


with file_open("text.txt") as f_open:
    print("file processing")
