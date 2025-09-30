class Stack:
    def __init__(self, max_size=None):
        self._items = []
        self.max_size = max_size

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def push(self, item):
        if self.max_size is not None and len(self._items) >= self.max_size:
            raise OverflowError("Stack is full (max_size reached).")
        try:
            self._items.append(item)
        except MemoryError:
            raise MemoryError("Failed to push: system out of memory.")

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def display(self):
        print(self._items)

stack = Stack(5)
stack.push(10)
stack.push(10)
stack.push(10)
stack.push(10)
stack.push(10)

stack.display()