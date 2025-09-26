from functools import wraps
from typing import Optional, List, Any

# ====== Decorator ======
def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Start: {func.__name__}\n")
        try:
            result = func(*args, **kwargs)
            print(f"\n[LOG] End: {func.__name__}")
            return result
        except Exception as e:
            print(f"\n[LOG] Error {func.__name__}: {e}")
            return None
    return wrapper


# ====== Students DB ======
students: List[dict] = []

def get_student_index_by_id(student_id: int) -> int:
    for i , s in enumerate(students):
        if s['id'] == student_id:
            return i
    return -1

# ====== Basics Functions ======

# ====== Add Student ======
@log_action
def add_student(student_id: int, name: str, age: int, grades: list[int]) -> bool:
    """Add New Student Without Repeat ID"""
    if get_student_index_by_id(student_id) != -1:
        print('This ID is Already Exists')
        return False
    name = name.strip()
    if not name:
        print('Must Add Name!!')
        return False
    students.append({
        'id': student_id,
        'name': name,
        'age': age,
        'grades': grades
    })
    print('<<ADDED DONE>>')
    return True

# ====== Calculate AVG ======
def calculate_avg(grades: list[int]) -> float:
    """Calculate Avg Grades Safe"""
    return(sum(grades) / len(grades)) if grades else 0.0


# ====== Display Students ======
def display_students() -> None:
    """Display Students With Grades"""
    if not students:
        print('No Students Find!!')
        return

    for s in sorted(students, key=lambda x: x['id']):
        avg = calculate_avg(s['grades'])
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grades: {s['grades']} | Grades AVG: {avg:.2f}")


# ====== Update Students ======
@log_action
def update_student(student_id: int, new_name: Optional[str] = None, new_age: Optional[int] = None) -> bool:
    """Update Student Name/Age"""
    idx = get_student_index_by_id(student_id)
    if idx == -1:
        print('No Student Find!!')
        return False
    if new_name is not None and new_name.strip():
        students[idx]['name'] = new_name.strip()
    if new_age is not None:
        students[idx]['age'] = new_age
    print('<<Updated DONE>>')
    return True

# ====== Delete Students ======
@log_action
def delete_student(student_id: int) -> bool:
    """Delete Student By ID"""
    idx = get_student_index_by_id(student_id)
    if idx == -1:
        print('No Student Find!!')
        return False
    del students[idx]
    print('<<Deleted DONE>>')
    return True

# ====== Search for a Student ======
def search_student(name: str) -> Optional[dict]:
    """Search By Student Name"""
    name = name.strip().lower()
    found = [s for s in students if s['name'] == name]
    if not found:
        print('No Student Find!!')
        return None
    s = found[0]
    print(f'Found ({s['name']}): Age: {s['age']} | Grades AVG: {calculate_avg(s['grades']):.2f}')
    return s

# ====== Closure Filter By Age ======
def make_filter(min_age: int):
    def filter_student():
        return [s for s in students if s['age'] >= min_age]
    return filter_student

# ====== Safe Input For ID & Age ======
def safe_input(prompt: str, allow_empty: bool = False, min_val: Optional[int] = None, max_val: Optional[int] = None) -> Optional[int]:
    while True:
        val = input(prompt).strip()
        if allow_empty and val == '':
            return None
        try:
            n = int(val)
            if min_val is not None and n < min_val:
                print(f'must be >= {min_val}')
                continue
            if max_val is not None and n > max_val:
                print(f'must be <= {max_val}')
                continue
            return n
        except ValueError:
            print('Enter a positive int Number!!!')

# ====== Safe Input Grades ======
def input_grades() -> None | list[dict] | list[Any]:
    while True:
        raw = input('Enter Grades with space between them or make it empty:')
        if raw == '':
            return []
        parts = raw.split()
        try:
            grades = [int(x) for x in parts]
            if any(g < 0 or g > 100 for g in grades):
                print('must be between 0 and 100!!!')
                continue
            return grades
        except ValueError:

            print('Enter a positive int number with space between them!!!')

# print(add_student(1, 'zeyad', 25, [83,23,0]), students)
# print(add_student(2, 'salem', 22, [83,2,54]), students)
# print(add_student(3, 'ahmed', 10, [3,23,54]), students)
# print(add_student(4, 'ghaleb', 30, [83,23,4]), students)
# print(add_student(5, 'mama', 40, [8,23,5]), students)
# display_students()
# search_student('mama')

# ====== Main Menu ======
def main():
    menu = '''
    ==== Students Management System ====
    (a) ADD Student.
    (w) WATCH Students.
    (u) UPDATE Student.
    (s) SEARCH for a Student.
    (f) FILTER By Age.
    (d) DELETE Student.
    (x) Exit.
    '''
    try:
        while True:
            print(menu)
            choice = input('Choice a Process:').strip()

            if choice == 'a'.strip().lower():
                sid = safe_input('ID:', min_val=1)
                name = input('Name:')
                age = safe_input('Age:', min_val=6)
                grades = input_grades()
                add_student(sid, name, age, grades)

            elif choice == 'w':
                display_students()

            elif choice == 'u'.lower():
                sid = safe_input('Enter Student ID:', min_val=1)
                new_name = input('New Name or (Press Enter):').strip()
                new_age = safe_input('New Age or (Press Enter):', min_val=6)
                update_student(sid, new_name if new_name else None, new_age)

            elif choice == 's':
                name = input('Enter the Student Name:')
                search_student(name)

            elif choice == 'f':
                min_age = safe_input('The Min Age:', min_val=6)
                result = make_filter(min_age)()
                if result:
                    for s in result:
                        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Grades AVG: {calculate_avg(s['grades']):.2f}")
                else:
                    print('Not Found!!!')

            elif choice == 'd':
                sid = safe_input('Enter Student ID:', min_val=1)
                delete_student(sid)

            elif choice == 'x':
                print('Bye Bye')
                break

            else:
                print('Wrong Choice, try Again')

    except KeyboardInterrupt:
        print('\n The program has shut, bye!.')



# ====== Run Program ======

main()