class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


def insert(root, item):
    if root is None:
        return

    q = [root]

    while len(q):
        root = q[0]
        q.pop(0)

        if not root.left:
            root.left = Node(item)
            break
        else:
            q.append(root.left)

        if not root.right:
            root.right = Node(item)
            break
        else:
            q.append(root.right)



if __name__ == '__main__':
    roots = Node(5)
    roots.left = Node(10)
    roots.left.left = Node(2)
    roots.right = Node(20)
    roots.right.left = Node(8)
    roots.right.right = Node(14)

    print("Inorder traversal before insertion:", end = " ")
    inorder(roots)


    value = 3
    insert(roots, value)

    print("\nInorder traversal after insertion:", end = " ")
    inorder(roots)

    roots.left.left.right = Node(44)
    roots.right.right.left = Node(33)

    print()
    inorder(roots)

    roots.left.left.left = Node(55)
    roots.right.right.right = Node(66)

    print()
    inorder(roots)