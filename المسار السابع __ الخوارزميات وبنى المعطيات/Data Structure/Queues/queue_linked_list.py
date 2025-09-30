class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return True if self.front is None else False

    def enqueue(self, item):
        new_node = Node(item)

        if self.rear is None:
            self.front = self.rear = new_node


        self.rear.next = new_node
        self.rear = new_node
        print(item)

    def dequeue(self):
        if self.front == 0:
            return self.is_empty()

        temp = self.front
        self.front = temp.next

        if self.front is None:
            self.rear = None

        return f"Dequeue item is {temp.data}"

    def display(self):
        item = self.front
        while item:
            print(item.data)
            item = item.next



if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.display()
    print(q.is_empty())