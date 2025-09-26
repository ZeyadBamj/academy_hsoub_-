from employee import Employee
from manager import Manager
from programmer import Programmer
from freelancer_programmer import FreelancerProgrammer
from roles import *
from payments import *
from designer import Designer


if __name__ == '__main__':
    ahmed = Programmer('Ahmed', 'Jameel', 3000, 'PHP', ['Web', 'Blog'])
    ali = FreelancerProgrammer('Ali', 'Mazin', 200, 18, 'C#', ['App', 'Desktop'])
    mazin = Programmer.from_string('Mazin/Saleh/7000/Dart')
    print(ahmed.info())
    print(mazin.info())
    print(ahmed.get_projects())

    employees = [
        FreelancerProgrammer('Salem', 'Slim', 200, 10, 'C', ['Web', 'App']),
        Programmer('Odi', 'Taha', 2000, 'Rust', ['Desktop', 'Cloud'])
    ]

    zezo = Manager('Zezo', 'Zero', 8000, employees)

    print(zezo.get_employees())

    sarah = Designer('Sarah', 'Khaled', 5000, 4, ['Drawing', 'Photoshop'])
    print(sarah.info())

# Designer , DesignerRole