from __future__ import annotations
from copy import copy

class Book:
    def __init__(self, name = None, author = None, pages = None):
        self.name = name
        self.author = author
        self.pages = pages

    def clone(self) -> Book:
        return copy(self)


if __name__ == "__main__":
    book1 = Book("Dive into Design Patterns", "Alexander Shvets", 409)
    book2 = Book("Eloquent JS", "Marign Haverbeke", 472)
    book3 = Book("Dive into Refactoring", "Alexander Shvets", 336)

    cloned1 = book1.clone()

    books = [book1 ,book2, book3]

    clones = []

    for item in books:
        if item.author == "Alexander Shvets":
            cloned_book = item.clone()
            clones.append(cloned_book)
            print("Copied: ", cloned_book.name)


    cloned1.author = 'zeyad'
    print(cloned1.author)
    print(book1.author)