class ProgrammerRole:
    def __init__(self, lang, projects):
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def assign_project(self, proj):
        self.projects.append(proj)

    def get_projects(self):
        print("\n\nProjects:")
        print('=' * 10)
        projects_list = []
        for i, proj in enumerate(self.projects):
            projects_list.append(f'{i + 1}. {proj}')
        return "\n".join(projects_list) + "\n\n"

class ManagerRole:
    def __init__(self, employees = None):
        if employees is None:
            employees = []
        self.employee = employees

    def get_employees(self):
        print("\n\nEmployees:")
        print('=' * 10)
        employees_list = []
        for i, emp in enumerate(self.employee):
            employees_list.append(f'{i + 1}. {emp.info()}')
        return "\n".join(employees_list) + "\n\n"


class DesignerRole:
    def __init__(self, exper_years, apps):
        self.exper = exper_years
        self.apps = apps

    def exper_years(self):
        return self.exper

    def assign_projects(self, app):
        self.apps.append(app)
