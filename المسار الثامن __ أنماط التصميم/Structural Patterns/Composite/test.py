from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    def add(self, component: Component):
        pass

    def remove(self, component: Component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf Component"

class Composite(Component):
    def __init__(self):
        self._children: List[Component] = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def is_composite(self):
        return True

    def operation(self):
        result = []
        for child in self._children:
            result.append(child.operation())
        return f"Branch({'+'.join(result)})"


def client_code(component: Component):
    print(f"Result: {component.operation()}", end="")

def client_2(component1: Component, component2: Component):
    if component1.is_composite():
        component1.add(component2)
    print(f"Result: {component1.operation()}", end="")