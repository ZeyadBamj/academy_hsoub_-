from freelancer import Freelancer
from programmer import Programmer


class FreelancerProgrammer(Freelancer, Programmer):
    def __init__(self, f_name, l_name, hour_rate, work_hours, lang, projects):
        Freelancer.__init__(self, f_name, l_name, hour_rate, work_hours)
        Programmer.__init__(self, f_name, l_name, lang, projects)
