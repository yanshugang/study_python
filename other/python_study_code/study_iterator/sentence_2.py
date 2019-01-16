"""
使用迭代器模式实现
"""

import re
import reprlib

RE_WORD = re.compile("\w+")


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1

        return word

    def __iter__(self):
        return self


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

s = Sentence("hello world")
i = s.__iter__()

print(i.__next__())
print(i.__next__())
print(i.__next__())