from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class WordsIterator(Iterator):
    def __init__(self, collection: WordsCollection, reverse: bool = False):
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self):
        if self._position < 0 or self._position >= len(self._collection):
            raise StopIteration()

        value = self._collection.collection[self._position]

        self._position += -1 if self._reverse else 1

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = None):
        if collection is None:
            collection = []
        self.collection = collection

    def __iter__(self) -> WordsIterator:
        return WordsIterator(self, reverse=False)

    def get_reverse_iterator(self) -> WordsIterator:
        return WordsIterator(self, reverse=True)

    def add_item(self, item: Any):
        self.collection.append(item)

    def __len__(self):
        return len(self.collection)


if __name__ == "__main__":
    collections = WordsCollection()
    collections.add_item("First")
    collections.add_item("Second")
    collections.add_item("Third")

    print("Straight Traversal:")
    print("\n".join(collections))

    print("\nReverse Traversal:")
    print("\n".join(collections.get_reverse_iterator()))
