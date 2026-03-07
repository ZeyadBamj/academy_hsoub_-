from abc import ABC, abstractmethod

class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f"car(seats={self.seats}, engine={self.engine}, gps={self.gps})"

class Manual:
    def __init__(self):
        self.text = ""

    def add(self, line):
        self.text += line + "\n"

    def __str__(self):
        return self.text


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, number):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self):
        pass

    @abstractmethod
    def set_gps(self):
        pass




class CarBuilder(Builder):
    def reset(self):
        self.car = Car()

    def set_seats(self, number):
        self.car.seats = number

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self):
        self.car.trip_computer = True

    def set_gps(self):
        self.car.gps = True

    def get_result(self):
        return self.car

class CarManualBuilder(Builder):
    def reset(self):
        self.manual = Manual()

    def set_seats(self, number):
        self.manual.add(f"The car has {number} seats.")

    def set_engine(self, engine):
        self.manual.add(f"Engine type: {engine}")

    def set_trip_computer(self):
        self.manual.add("Includes trip computer.")

    def set_gps(self):
        self.manual.add("include GPS system.")

    def get_result(self):
        return self.manual


class Director:
    @staticmethod
    def make_sports_car(builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("V8")
        builder.set_trip_computer()
        builder.set_gps()

    @staticmethod
    def make_suv(builder):
        builder.reset()
        builder.set_seats(5)
        builder.set_engine("V6")
        builder.set_gps()



director = Director()

carB = CarBuilder()
director.make_sports_car(carB)
car = carB.get_result()

print("The Car: ")
print(car)


manualB = CarManualBuilder()
director.make_sports_car(manualB)
manual = manualB.get_result()

print("\nCar Manual: ")
print(manual)