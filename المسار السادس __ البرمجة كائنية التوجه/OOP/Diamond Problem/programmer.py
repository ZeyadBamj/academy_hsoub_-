from employee import Employee
from roles import *
from payments import *

class Programmer(Employee, ProgrammerRole, Salary):
    def __init__(self, f_name, l_name, salary, lang, projects = None):
        Salary.__init__(self, salary)
        ProgrammerRole.__init__(self, lang, projects)
        Employee.__init__(self, f_name, l_name)


    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}; Salary: {self.salary}; Lang: {self.lang}"

    def calculate_salary(self):
        return Salary.calculate_salary(self)

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary, lang = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary, lang)

