from abc import ABC, abstractmethod
from typing import Any


class Car:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Car Parts: {', '.join(self.parts)}", end="")


class Manual:
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Manual Parts: {', '.join(self.parts)}", end="")


class Builder(ABC):
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def part_a(self):
        pass

    @abstractmethod
    def part_b(self):
        pass

    @abstractmethod
    def part_c(self):
        pass


class CarBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def product(self) -> Car:
        car = self._product
        self.reset()
        return car

    def part_a(self):
        self._product.add("A Car")

    def part_b(self):
        self._product.add("B Car")

    def part_c(self):
        self._product.add("C Car")


class ManualBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Manual()

    @property
    def product(self) -> Manual:
        manual = self._product
        self.reset()
        return manual

    def part_a(self):
        self._product.add("A Manual")

    def part_b(self):
        self._product.add("B Manual")

    def part_c(self):
        self._product.add("C Manual")


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_basic_product(self):
        self._builder.part_a()

    def build_full_featured(self):
        self._builder.part_a()
        self._builder.part_b()
        self._builder.part_c()


if __name__ == "__main__":
    CarDirector = Director()
    ManualDirector = Director()

    CarB = CarBuilder()
    ManualB = ManualBuilder()

    CarDirector.builder = CarB
    ManualDirector.builder = ManualB

    print("Standard Basic Car: ")
    CarDirector.build_basic_product()
    CarB.product.list_parts()
    print('\n')

    print("Standard Basic Manual: ")
    ManualDirector.build_basic_product()
    ManualB.product.list_parts()
    print('\n')

    print("Standard Full Feature Car: ")
    CarDirector.build_full_featured()
    CarB.product.list_parts()
    print('\n')

    print("Standard Full Feature Manual: ")
    ManualDirector.build_full_featured()
    ManualB.product.list_parts()
    print('\n')

    print("Custom Car: ")
    CarB.part_a()
    CarB.part_b()
    CarB.product.list_parts()
    print('\n')

    print('Custom Manual: ')
    ManualB.part_a()
    ManualB.part_b()
    ManualB.product.list_parts()