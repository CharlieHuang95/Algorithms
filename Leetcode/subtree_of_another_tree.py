# Subtree of Another Tree

# This question asks if, a tree (t) is the subtree of another tree (s).
# This can be solved by recursively visiting the nodes of the larger
# tree (s), and checking to see if the node matches the root of tree (t).
# If they contain the same value, then we have a candidate for a matching
# tree. We can then check whether the two trees are equivalent by calling
# a helper function.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t:
            return True
        if not s:
            return False
        return self.isSubtree_helper(s, t)
       
    def isSubtree_helper(self, s, t):
        if not s or not t:
            return False
        if t.val == s.val and self.isSameTree(s, t):
            return True
        return self.isSubtree_helper(s.left, t) or self.isSubtree_helper(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if s and t:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right) and s.val == t.val
        return False
