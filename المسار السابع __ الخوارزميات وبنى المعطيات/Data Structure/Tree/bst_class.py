class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None


    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.data, end=' ')
            self._inorder(root.right)

    def inorder(self):
        self._inorder(self.root)


    def _insert(self, root, node):
        if node.data < root.data:

            if root.left is None:
                root.left = node

            else:
                self._insert(root.left, node)

        elif node.data > root.data:

            if root.right is None:
                root.right = node

            else:
                self._insert(root.right, node)

        else:
            print(f'Number {root.data} Repeated')


    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node

        else:
            self._insert(self.root, new_node)

    def search(self, item):
        current = self.root
        while current is not None:
            if current.data == item:
                return f"{item} is Root" if current is self.root else item
            elif item < current.data:
                current = current.left
            else:
                current = current.right
        return None


    @staticmethod
    def _min_value_node(current):
        while current.left is not None:
            current = current.left

        return current

    def _delete_node(self, root, item):
        if root is None:
            return root

        if item < root.data:
            root.left = self._delete_node(root.left, item)

        elif item > root.data:
            root.right = self._delete_node(root.right, item)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                temp = self._min_value_node(root.right)
                root.data = temp.data
                root.right = self._delete_node(root.right, temp.data)

        return root

    def delete(self, item):
        self.root = self._delete_node(self.root, item)


bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:")
bst.inorder()

# البحث
x = bst.search(50)
print("\n\nSearch:", f"Found {x}" if x else "Not Found")

# الحذف
print("\nDelete 20")
bst.delete(20)
bst.inorder()

print("\n\nDelete 30")
bst.delete(30)
bst.inorder()

print("\n\nDelete 80")
bst.delete(80)
bst.inorder()
print("\n\nDelete 70")
bst.delete(70)
bst.inorder()
print("\n\nDelete 60")
bst.delete(60)
bst.inorder()
print("\n\nDelete 50")
bst.delete(50)
bst.inorder()
print("\n\nDelete 40")
bst.delete(40)
bst.inorder()

