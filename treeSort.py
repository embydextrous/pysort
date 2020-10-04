class Node:
    def __init__(self, data):
        self.count = 1
        self.data = data
        self.left = None
        self.right = None

# Assuming all elements are distinct
def treeSort(a):
    n = len(a)
    if n == 0:
        return
    root = Node(a[0])
    for i in range(1, len(a)):
        insertIntoBST(root, a[i])
    inorder(root, a, [0])

def inorder(root, a, index):
    if root:
        inorder(root.left, a, index)
        for i in range(root.count):
            a[index[0]] = root.data
            index[0] += 1
        inorder(root.right, a, index)

def insertIntoBST(root, n):
    if root.data == n:
        root.count += 1
    elif n < root.data:
        if root.left:
            insertIntoBST(root.left, n)
        else:
            root.left = Node(n)
    else:
        if root.right:
            insertIntoBST(root.right, n)
        else:
            root.right = Node(n)

a = [6, 3, 9, 1, 0, 3, 5, 1, 4, 2]
treeSort(a)
print a