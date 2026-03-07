from copy import deepcopy

class Author:
    def __init__(self, name, country):
        self.name = name
        self.country = country

class Book:
    def __init__(self, name, author: Author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    author1 = Author("Alexander Shvets", "USA")

    book1 = Book("Design Patterns", author1, 400)
    book2 = book1.clone()

    book1.author.country = "EU"

    book2.author.name = "Changed"

    print(book1.author.name)
    print(book2.author.name)
    print(book2.author.country)
    print(book1.author.country)
