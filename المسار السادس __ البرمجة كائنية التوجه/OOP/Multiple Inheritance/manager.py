from employee import Employee


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
