from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, Any


class WordsIterator(Iterator):
    def __init__(self, collection: WordsCollection, reverse: bool = None):
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self):
        if self._position < 0 or self._position >= len(self._collection):
            raise StopIteration

        value = self._collection.collection[self._position]

        self._position += -1 if self._reverse else 1

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = None):
        if collection is None:
            collection = []

        self.collection = collection

    def __iter__(self):
        return WordsIterator(self, False)

    def get_reverse(self):
        return WordsIterator(self, True)

    def add_item(self, item: Any):
        self.collection.append(item)

    def __len__(self):
        return len(self.collection)

if __name__  == "__main__":
    collec = WordsCollection()
    collec.add_item("a")
    collec.add_item("b")
    collec.add_item("c")

    print("Straight")
    print("\n".join(collec))

    print("Reverse")
    print("\n".join(collec.get_reverse()))
