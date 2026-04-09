from enum import Enum

class Day(Enum):
    FRIDAY = 1
    SATURDAY = 2
    SUNDAY = 3
    MONDAY = 4
    TUESDAY = 5
    WEDNESDAY = 6
    THURSDAY = 7

print(list(Day))