class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity


    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print('Fully')
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print(f"EnQueue to Queue {item}")

    def dequeue(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        print(f'DeQueue from Queue {self.front}')
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

    def front_item(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        print(f'Front item in Queue {self.Q[self.front]}')

    def rear_item(self):
        if self.is_empty():
            print('Queue is Empty')
            return
        print(f'Rear item in Queue {self.Q[self.rear]}')

    def display(self):
        print(self.Q)


if __name__ == '__main__':

    queue = Queue(3)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.front_item()
    queue.rear_item()
    queue.display()