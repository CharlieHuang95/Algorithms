# Given a binary tree, determine if it is height balanced

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_balanced(root):
    def dfs(node):
        if not node:
            return (0, True)
        height_l, is_balanced_l = dfs(node.left)
        height_r, is_balanced_r = dfs(node.right)
        depth = max(height_l, height_r) + 1
        if not is_balanced_l or not is_balanced_r:
            return (depth, False)
        return (depth, abs(height_l - height_r) < 2)
    return dfs(root)[1]

if __name__=="__main__":
    root = Node(5)
    assert(is_balanced(root))
    root.left = Node(3)
    assert(is_balanced(root))
    root.left.left = Node(2)
    assert(not is_balanced(root))
    root.right = Node(7)
    assert(is_balanced(root))
    print "Success"
