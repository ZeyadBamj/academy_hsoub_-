from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Publisher:
    state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer):
        print("Publisher: Attached on Observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        print("Publisher: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self):
        print("\nPublisher: I'm doing something important.")
        self.state = randrange(0, 10)
        print(f"Publisher: My state has just changed to: {self.state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, publisher: Publisher):
        pass

class ConcreteObserverA(Observer):
    def update(self, publisher: Publisher):
        if publisher.state < 3:
            print("A: Reacted to the event")

class ConcreteObserverB(Observer):
    def update(self, publisher: Publisher):
        if publisher.state == 0 or publisher.state >= 3:
            print("B: Reacted to the event")


if __name__ == "__main__":
    publish = Publisher()

    obser_a = ConcreteObserverA()
    publish.attach(obser_a)

    obser_b = ConcreteObserverB()
    publish.attach(obser_b)

    publish.some_business_logic()
    publish.some_business_logic()