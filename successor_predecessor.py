class Node:
    def __init__(self, val: int, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(node: Node):
    # If right child exists, successor is leftmost node of right subtree
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    # Otherwise, move up until coming from left child
    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent

def find_predecessor(node: Node):
    # If left child exists, predecessor is rightmost node of left subtree
    if node.left:
        node = node.left
        while node.right:
            node = node.right
        return node
    # Otherwise, move up until coming from right child
    while node.parent and node == node.parent.left:
        node = node.parent
    return node.parent

# Example BST
a = Node(10)
b = Node(5, parent=a)
c = Node(15, parent=a)
d = Node(2, parent=b)
e = Node(12, parent=c)
f = Node(20, parent=c)

a.left = b
a.right = c
b.left = d
c.left = e
c.right = f

# Test node
node = c  # 15
pred = find_predecessor(node)
succ = find_successor(node)

print(f"next smallest: {pred.val if pred else None}, next largest: {succ.val if succ else None}")
