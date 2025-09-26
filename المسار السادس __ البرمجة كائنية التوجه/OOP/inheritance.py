import datetime

class Employee:
    __salary_raise = 1.1

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.__salary = salary

    def info(self):
        return f"Name: {self.f_name} {self.l_name} | Salary: {self.__salary}"

    @property
    def salary(self):
        return self.__salary * self.__salary_raise

    @salary.setter
    def salary(self, val):
        if val <= 0 or val > 10000:
            raise ValueError
        self.__salary = val

    @classmethod
    def __change_raise(cls, amount):
        try:
            if amount < 0 or amount > 5:
                raise ValueError
            cls.__salary_raise = amount
        except Exception as e:
            print(f"Can't raise Salary to {amount}{e}")

    @classmethod
    def salary_raise(cls, amount):
        return cls.__change_raise(amount)

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary)


    @staticmethod
    def is_workday(d):
        if d.weekday() == 4 or d.weekday() == 5:
            return False
        return True



ahmed = Employee('ahmed', 'mubarak', 2000)
ali = Employee.from_string('salem/ghaleb/1000')
print(ali.info())

ahmed.salary_raise(20)
print(ahmed.salary)
print(ahmed.info())

date = datetime.date(2025, 9, 8)
print(ahmed.is_workday(date))

class Manager(Employee):
    def __init__(self, f_name, l_name, salary, employee):
        super().__init__(f_name, l_name, salary)
        self.employee = employee

    def get_employees(self):
        print('\n\nEmployees:')
        print('='*10)
        employees_list = []
        for i, emp in enumerate(self.employee):
            employees_list.append(f'{i + 1}. {emp.info()}')
        return "\n".join(employees_list) + "\n\n"
    
    
    
salem = Employee('Salem', 'Ali', 3000)
john = Employee('John', 'Mike', 2000)
sosa = Employee('Sosa', 'Taha', 4000)

yzeed = Manager('Yzeed', 'Mubarak', 7000, [salem, john, sosa])

print(yzeed.get_employees())



  # add two features to programmer: 1- lang,  2- projects
class Programmer(Employee):
    def __init__(self, f_name, l_name, salary, lang, projects):
        super().__init__(f_name, l_name, salary)
        self.lang = lang
        self.projects = projects

    def get_projects(self):
        for i, n in enumerate(self.projects):
            print(f'------ Project {i + 1} ------')
            print(n)
        return "="* 30

class Project:
    #name, desc, days, done with t or f
    def __init__(self, name, desc, days, done):
        self.name = name
        self.desc = desc
        self.days = days
        self.done = done

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Description: {self.desc}\n"
                f"Days: {self.days}\n"
                f"Done: {self.done}")


my_projects = [
Project('Weather App', 'See the Condition of Weather', 14, True),
Project('Library Web', 'Choose the book that you want', 20, False),
Project('Deliver App', 'Deliver what you want', 60, True),
]

zeyad = Programmer('Zeyad', 'Mubarak', 7000, 'Dart', my_projects)
print(zeyad.get_projects())