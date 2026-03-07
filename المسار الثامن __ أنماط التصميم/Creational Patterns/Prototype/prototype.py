from __future__ import annotations
from copy import copy

class Book:
    def __init__(self):
        self._name = None
        self._author = None
        self._pages = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        self._pages = value

    def clone(self) -> Prototype:
        self.name = copy(self.name)
        self.author = copy(self.author)
        self.pages = copy(self.pages)
        return copy(self)

if __name__ == "__main__":
    book1 = Book()
    book1.name = "Dive into design patterns"
    book1.author = "Alexander Shvets"
    book1.pages = 409

    book2 = Book()
    book2.name = "Eloquent Javascript"
    book2.author = "Marign Haverbeke"
    book2.pages = 472

    book3 = Book()
    book3.name = "Dive into Refactoring"
    book3.author = "Alexander Shvets"
    book3.pages = 336

    list = []
    list.append(book1)
    list.append(book2)
    list.append(book3)

    for item in list:
        if item.author == "Alexander Shvets":
            item.clone()
            print('yes,,,,', item.name)
