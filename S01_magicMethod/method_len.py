"""
魔术方法：__len__
"""


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(["tom", "bob", "jane"])

print(len(company))
