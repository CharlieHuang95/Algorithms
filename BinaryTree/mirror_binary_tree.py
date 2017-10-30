# Given a binary tree, find its mirror

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror_tree(root):
    if not root:
        return
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)

if __name__=="__main__":
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    mirror_tree(root)
    assert root.left.val == 7
    assert root.right.val == 3
    assert root.right.left.val == 4
    assert root.right.right.val == 2
    assert root.left.right is None
