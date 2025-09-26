from employee import Employee
from payments import Salary
from roles import ManagerRole

class Manager(Employee, ManagerRole, Salary):
    def __init__(self, f_name, l_name, salary, employees):
        ManagerRole.__init__(self, employees)
        Salary.__init__(self, salary)
        Employee.__init__(self, f_name, l_name)


    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}"

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary)
