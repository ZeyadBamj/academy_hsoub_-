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
        return "Leaf"

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

def client_2(component1: Component, component2:Component):
    if component1.is_composite():
        component1.add(component2)

    print(f"Result: {component1.operation()}", end="")


if __name__ == "__main__":
    simple = Leaf()
    print("Client: Simple Component:")
    client_code(simple)
    print('\n')

    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Composite Tree: ")
    client_code(tree)
    print('\n')

    print("Client: Composite Tree from Classes: ")
    client_2(tree, simple)
    print('\n')