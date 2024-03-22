class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    if root is None:
        return BinaryTreeNode(newValue)
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

root = None
root = insert(root, 50)
insert(root, 20)
insert(root, 53)

print("Root Node:", root.data)
print("Left Child of Root:", root.leftChild.data)
print("Right Child of Root:", root.rightChild.data)
