"""
生成器读大文件
500G, 1行,
"""


def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096)

        if not chunk:
            yield buf
            break
        buf += chunk


with open("./input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)
