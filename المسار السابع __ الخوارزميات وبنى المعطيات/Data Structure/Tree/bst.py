class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def insert(root,node):
    if root is None:
        return node

    if node.data < root.data:
        root.left = insert(root.left, node)

    elif node.data > root.data:
        root.right = insert(root.right, node)

    else:
        print(f'Number {root.data} Repeated!')

    return root


def search(root, item):
    if root is None or root.data == item:
        return f'root {item}'

    if root.data < item:
        return search(root.right, item)

    return search(root.left, item)

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left

    return current

def delete_node(root, item):
    if root is None:
        return root

    if item < root.data:
        root.left = delete_node(root.left, item)

    elif item > root.data:
        root.right = delete_node(root.right, item)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete_node(root.right, temp.data)

    return root




r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))
insert(r,Node(80))
insert(r,Node(80))


inorder(r)

x = search(r, 50)
if x is None:
    print('Not Found!')
else:
    print('Found {} in searching'.format(x))

print('\nDelete 20')
r = delete_node(r, 20)
print('Inorder traversal of the modified tree')
inorder(r)

print('\nDelete 30')
r = delete_node(r, 30)
print('Inorder traversal of the modified tree')
inorder(r)

print('\nDelete 80')
r = delete_node(r, 80)
print('Inorder traversal of the modified tree')
inorder(r)
