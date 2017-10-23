# Merge Two Binary Trees

# The two existing trees could overlap. These overlapping nodes
# will have their values summed up. Otherwise, we keep the non-null
# node for the new tree.

# Note that we can simply 
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return
        if not t1 or not t2:
            return t1 or t2
        t1.val += t2.val
        self.mergeTreesHelper(t1, t2)
        return t1

    def mergeTreesHelper(self, t1, t2):
        if t1.left and t2.left:
            t1.left.val += t2.left.val
            self.mergeTreesHelper(t1.left, t2.left)
        elif t1.left or t2.left:
            t1.left = (t1.left or t2.left)
        if t1.right and t2.right:
            t1.right.val += t2.right.val
            self.mergeTreesHelper(t1.right, t2.right)
        elif t1.right or t2.right:
            t1.right = (t1.right or t2.right)
