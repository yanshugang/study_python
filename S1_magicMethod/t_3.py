"""
魔法函数: __str__\__repr__
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        return ",".join(self.employee)

company = Company(["tom", "bob", "jane"])
print(company)
