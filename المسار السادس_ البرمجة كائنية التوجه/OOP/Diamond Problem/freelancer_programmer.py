from payments import HourlyPayment
from programmer import *
from roles import *


class FreelancerProgrammer(Employee, ProgrammerRole, HourlyPayment):
    def __init__(self, f_name, l_name, hour_rate, work_hours, lang, projects):
        HourlyPayment.__init__(self, work_hours, hour_rate)
        ProgrammerRole.__init__(self, lang, projects)
        Employee.__init__(self, f_name, l_name)

    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}; Work Hour: {self.work_hours}"

    def calculate_salary(self):
        return HourlyPayment.calculate_salary(self)