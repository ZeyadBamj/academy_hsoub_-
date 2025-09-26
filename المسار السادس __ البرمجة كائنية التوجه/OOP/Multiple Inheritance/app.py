from employee import Employee
from manager import Manager
from programmer import Programmer
from freelancer_programmer import FreelancerProgrammer

if __name__ == '__main__':
    # print(FreelancerProgrammer.__mro__)
    ali = FreelancerProgrammer('Ali', 'Mazin', 200, 5, 'PHP', ['Web', 'App'])
    print(ali.info())
    print(ali.calculate_salary())
    ali.assign_project('IOS App')
    print(ali.get_projects())