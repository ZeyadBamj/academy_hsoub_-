from employee import Employee
from payments import Salary
from roles import DesignerRole


class Designer(Employee, DesignerRole, Salary):
    def __init__(self, f_name, l_name, salary, exper_years, apps):
        Employee.__init__(self, f_name, l_name)
        DesignerRole.__init__(self, exper_years, apps)
        Salary.__init__(self, salary)

    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}; Experience: {self.exper}; Exper_Apps: {self.apps}"

    def calculate_salary(self):
        return Salary.calculate_salary(self)
