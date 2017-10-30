# Get Nth row of binary tree

import collections

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_nth_row_bfs(root, n):
    if not root:
        return []
    q = collections.deque()
    q.append(root)
    level = 1
    nodes = 1
    next_nodes = 0
    sol = []
    while q:
        node = q.popleft()
        if level == n:
            sol.append(node.val)
        if node.left:
            q.append(node.left)
            next_nodes += 1
        if node.right:
            q.append(node.right)
            next_nodes += 1
        nodes -= 1
        if nodes == 0:
            nodes = next_nodes
            next_nodes = 0
            level += 1
    return sol

def get_nth_row_dfs(root, n):
    def dfs(node, level):
        if not node:
            return
        if level == n:
            sol.append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    sol = []
    dfs(root, 1)
    return sol
            

if __name__=="__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(3)
    assert get_nth_row_bfs(root, 0) == [] == get_nth_row_dfs(root, 0)
    assert get_nth_row_bfs(root, 1) == [10] == get_nth_row_dfs(root, 1)
    assert get_nth_row_bfs(root, 2) == [5,15] == get_nth_row_dfs(root, 2)
    assert get_nth_row_bfs(root, 3) == [2,3] == get_nth_row_dfs(root, 3)
