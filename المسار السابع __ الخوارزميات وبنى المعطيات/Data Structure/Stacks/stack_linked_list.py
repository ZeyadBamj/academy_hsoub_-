class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:
    def __init__(self):
        self.top = None


    def is_empty(self):
        if self.top is None:
            return True
        return False

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f'{data} Pushed to Stack')

    def pop(self):
        if self.top is None:
            return self.is_empty()

        node = self.top
        self.top = self.top.next
        popped = node.data
        return popped


    def peek(self):
        if self.top is None:
            return self.is_empty()

        return self.top.data



stack = StackLL()
stack.push(10)
stack.push(20)
stack.push(30)

print(f'{stack.pop()} Popped from Stack')
print(f"{stack.peek()} is the Top")
