"""
生成器实现等差数列
"""


class ArithmeticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        # todo: type？？？
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        if forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index
