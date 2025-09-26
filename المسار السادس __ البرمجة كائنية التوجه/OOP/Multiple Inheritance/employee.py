from abc import ABC, abstractmethod



class Employee(ABC):
    __salary_raise = 1.1

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

    @classmethod
    @abstractmethod
    def from_string(cls, string):
        f_name, l_name, salary = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name)


    @staticmethod
    def is_workday(d):
        if d.weekday() == 4 or d.weekday() == 5:
            return False
        return True


