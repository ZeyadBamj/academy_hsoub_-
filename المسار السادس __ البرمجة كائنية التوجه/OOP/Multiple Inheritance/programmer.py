from employee import Employee


class Programmer(Employee):
    def __init__(self, f_name, l_name, salary, lang, projects = None):
        Employee.__init__(self, f_name, l_name)
        self.__salary = salary
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects


    def info(self):
        return f"Name: {self.f_name} {self.l_name}; Job Title: {self.__class__.__name__}"

    def calculate_salary(self):
        return self.__salary

    @classmethod
    def from_string(cls, string):
        f_name, l_name, salary, lang = string.split('/')
        salary = int(salary)
        return cls(f_name, l_name, salary, lang)

    def assign_project(self, project):
       self.projects.append(project)


    def get_projects(self):
        print("\n\nProjects:")
        print('='*10)
        projects_list = []
        for i, proj in enumerate(self.projects):
            projects_list.append(f'{i + 1}. {proj}')
        return "\n".join(projects_list) + "\n\n"
