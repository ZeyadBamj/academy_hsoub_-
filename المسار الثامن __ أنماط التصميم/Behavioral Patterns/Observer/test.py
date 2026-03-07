from __future__ import annotations
from random import randrange
from typing import List
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, publisher: Publisher):
        pass

class ObsA(Observer):
    def update(self, publisher: Publisher):
        if publisher.state < 4:
            print("A: Reacted to the Event")

class ObsB(Observer):
    def update(self, publisher: Publisher):
        if 4 <= publisher.state < 10:
            print("B: Reacted to the Event")


class Publisher:
    state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Attached on Subscriber")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print("Notify.....")
        for obser in self._observers:
            obser.update(self)

    def some_business_logic(self):
        print("\nPublisher")
        self.state = randrange(0, 10)
        print(f"Publisher: My state is {self.state}")
        self.notify()


if __name__ == "__main__":
    publish = Publisher()

    obser_a = ObsA()
    publish.attach(obser_a)

    obser_b = ObsB()
    publish.attach(obser_b)

    publish.some_business_logic()
    publish.some_business_logic()


