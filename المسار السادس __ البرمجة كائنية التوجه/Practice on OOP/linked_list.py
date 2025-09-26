class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert(prev_node, new_data):
        if prev_node is None:
            print('No item found!')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        item = self.head
        while item:
            print(item.data)
            item = item.next


    def delete(self, item):
        current = self.head

        if current is None:
            print('The List is Empty!')
            return

        if current.data == item:
            self.head = current.next
            print(f'Deleted the First Item: {item}')
            return

        prev = None
        while current and current.data != item:
            prev = current
            current = current.next

        if current is None:
            print(f'Can not find {item}')
            raise ValueError

        prev.next = current.next
        print(f'Deleted {item} Done.')
        return



ll = LinkedList()

first = Node(1)
second = Node(2)
third = Node(3)

ll.head = first

first.next = second
second.next = third
ll.push(0)
ll.insert(second, 2.5)

ll.append(10)
ll.delete(1)

ll.print_list()
