from employee import Employee


class Freelancer(Employee):
    def __init__(self, f_name, l_name, hour_rate, work_hours):
        Employee.__init__(self, f_name,l_name)
        self.hour_rate = hour_rate
        self.work_hours = work_hours

    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}; Work Hours: {self.work_hours}"

    def calculate_salary(self):
        return self.hour_rate * self.work_hours

    @classmethod
    def from_string(cls, string):
        f_name, l_name, hour_rate, work_hours = string.split('/')
        hour_rate, work_hours = int(hour_rate), int(work_hours)
        return cls(f_name, l_name, hour_rate, work_hours)
