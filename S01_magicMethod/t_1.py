"""
魔法方法: __getiterm__
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(["tom", "bob", "jane"])

for em in company:
    print(em)
