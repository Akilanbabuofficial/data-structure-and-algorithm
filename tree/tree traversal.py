class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder Traversal:", end=" ")
inorder_traversal(root)

print("\n preorder Traversal:", end=" ")
preorder_traversal(root)

print("\npostorder Traversal:", end=" ")
postorder_traversal(root)
