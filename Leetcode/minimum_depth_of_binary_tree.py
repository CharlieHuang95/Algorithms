# Minimum Depth of Binary Tree

# Given a binary tree, find the depth of the shallowest leaf node.

# This problem can be solved by traversing the binary tree in a
# breadth-first order.

import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        q = collections.deque()
        q.append(root)
        depth_q = collections.deque()
        depth_q.append(1)
        while q:
            cur_node = q.popleft()
            cur_depth = depth_q.popleft()
            if not cur_node.left and not cur_node.right:
                return cur_depth
            if cur_node.left:
                q.append(cur_node.left)
                depth_q.append(cur_depth + 1)
            if cur_node.right:
                q.append(cur_node.right)
                depth_q.append(cur_depth + 1)
