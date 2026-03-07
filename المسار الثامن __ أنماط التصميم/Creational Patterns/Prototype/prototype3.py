from copy import copy

class Book:
    def __init__(self, name = None, author = None, pages = None):
        self.name = name
        self.author = author
        self.pages = pages

    def clone(self):
        return copy(self)


class PrototypeRegistry:
    def __init__(self):
        self._item = {}

    def register(self, key: str, prototype: Book):
        self._item[key] = prototype

    def unregister(self, key: str):
        del self._item[key]

    def clone(self, key: str) -> Book:
        return self._item[key].clone()

if __name__ == "__main__":
    registry = PrototypeRegistry()

    book1 = Book("Design Patterns", "Alexander Shvets", 300)
    book2 = Book("Eloquent JavaScript", "Marijn Haverbeke", 450)

    registry.register("pattern", book1)
    registry.register("javascript", book2)

    clone1 = registry.clone("pattern")
    clone2 = registry.clone("javascript")

    print(clone1.name)
    print(clone2.name)