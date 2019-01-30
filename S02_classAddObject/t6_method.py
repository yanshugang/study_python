"""
静态方法、类方法、对象方法
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def tomorrow(self):
        self.day += 1

    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))  # tuple可以直接解包
        return Date(int(year), int(month), int(day))  # 静态方法，此处使用硬编码，如果Date类名改了，此处也需要手动修改。

    # 类方法，直接传递class
    @classmethod
    def from_string(cls, data_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))  # 声明类方法，与静态方法相比，更加灵活

    # 判断传入的字符串是否合法
    @staticmethod
    def valid_str(data_str):
        year, month, day = tuple(data_str.split("-"))
        if int(year) > 0 and int(month) > 0 and int(month) <= 12 and int(day):
            return True

    # 定义__str__方法，可以实现当print时直接按规定格式打印
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,
                                             month=self.month,
                                             day=self.day)


if __name__ == '__main__':
    new_day = Date(2019, 1, 19)
    new_day.tomorrow()
    print(new_day)

    data = "2018-12-19"
    new_day = Date.parse_from_string(data)
    print(new_day)

    new_day = Date.from_string(data)
    print(new_day)

    print(Date.valid_str(data))
