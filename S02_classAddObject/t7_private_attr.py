"""
私有属性
"""


class User:
    def __init__(self, birthday):
        self.birthday = birthday

    def get_age(self):
        # 返回年龄
        return 2018 - self.birthday.year
