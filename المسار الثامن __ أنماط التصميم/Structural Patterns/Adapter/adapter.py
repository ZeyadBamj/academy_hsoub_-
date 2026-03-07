from __future__ import annotations
import math

class RoundHole:
    def __init__(self, radius: int):
        self.__radius = radius

    def get_radius(self) -> int:
        return self.__radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()

class RoundPeg:
    def __init__(self, radius: int):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

class SquarePeg:
    def __init__(self, width: int):
        self.__width = width

    def get_width(self) -> int:
        return self.__width

class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg):
        self.__peg = peg

    def get_radius(self):
        return (self.__peg.get_width() * math.sqrt(2)) / 2


if __name__ == "__main__":
    hole = RoundHole(5)
    rPeg = RoundPeg(5)
    print(hole.fits(rPeg))

    small_sq = SquarePeg(5)
    large_sq = SquarePeg(10)

    small_sq_Adapter = SquarePegAdapter(small_sq)
    large_sq_Adapter = SquarePegAdapter(large_sq)
    print(hole.fits(small_sq_Adapter), hole.fits(large_sq_Adapter))
