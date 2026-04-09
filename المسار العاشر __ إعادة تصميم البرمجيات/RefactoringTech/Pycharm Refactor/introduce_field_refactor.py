import math

class SolverEquation:
    def demo(self):
        a = 3
        b = 25
        c = 46

        self.math_sqrt = math.sqrt(b ** 2 - 4 * a * c)
        root1 = (-b + self.math_sqrt) / (2 * a)
        root2 = (-b - self.math_sqrt) / (2 * a)
