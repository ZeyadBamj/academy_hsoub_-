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


class Manager(Employee):
    def __init__(self, f_name, l_name, salary, employees = None):
        super().__init__(f_name, l_name)
        self.__salary = salary
        if employees is None:
            employees = []
        self.employee = employees

    def get_employees(self):
        print("\n\nEmployees:")
        print('='*10)
        employees_list = []
        for i, emp in enumerate(self.employee):
            employees_list.append(f'{i + 1}. {emp.info()}')
        return "\n".join(employees_list) + "\n\n"

    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}"

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary)


# class Programmer(Employee):
#     def __init__(self, f_name, l_name, salary, lang, projects = None):
#         super().__init__(f_name, l_name)
#         self.__salary = salary
#         self.lang = lang
#         if projects is None:
#             projects = []
#         self.projects = projects
#
#
#     def info(self):
#         return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}"
#
#     def calculate_salary(self):
#         return self.__salary
#
#     @classmethod
#     def from_string(cls, string):
#         f_name, l_name, salary, lang = string.split('/')
#         salary = int(salary)
#         return cls(f_name, l_name, salary, lang)
#
#     def assign_project(self, project):
#        self.projects.append(project)
#
#     def get_projects(self):
#         return self.projects
#
# ahmed = Programmer('ahmed', 'khaled', 3000, 'Dart', ['Web', 'App', 'DeskTop'])
# print(ahmed.info())
# print(ahmed.get_projects())



class Accountant(Employee):
    def __init__(self, f_name, l_name, salary, experience_years, department):
        super().__init__(f_name, l_name)
        self.__salary = salary
        self.exper_years = experience_years
        self.depart = department

    def info(self):
        return f"Name: {self.f_name} {self.l_name}; \nJob Title: {self.__class__.__name__}; \nExperience: 3 years;"

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary, experience_years, department = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary, experience_years, department)



ali = Accountant.from_string('Ali/Sami/3000/4/Accounts')
print(ali.info())
