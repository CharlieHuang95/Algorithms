# Get Nth row of binary tree

# This problem can be solved using bfs and dfs. To use bfs, we keep track
# of how many nodes there are at every subsequent level. We only add valid
# nodes to the queue, and maintain a counter to know when the current level
# is traversed. To use dfs, we pass the current depth on each recursive node
# and we only add to a global solution variable if the current depth is
# the desired depth n.

# Assuming that the binary tree is balanced, the runtime for both is O(N)
# because we traverse each node only once. The memory complexity is O(N)
# for bfs because the final row could potentially be half of the entire tree,
# meaning that we have to store a number of nodes comparable to the size of
# the tree within our queue. The memory complexity of dfs is O(logN) because
# the stack only needs to be as deep as the longest path from root to leaf,
# which is logN for a balanced tree.

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
