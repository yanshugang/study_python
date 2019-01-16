"""
定义一个sentence类，通过索引从文本中提取单词
"""

import re
import reprlib

# todo: 这个正则是怎么用的？？？
RE_WORD = re.compile("\w+")


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        # todo: reprlib.repr???
        return "Sentence(%s)" % reprlib.repr(self.text)


s = Sentence("hello world")
print(s.text)
print(s.words)
print(s)
