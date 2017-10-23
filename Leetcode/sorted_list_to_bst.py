# Sorted List to BST

# There appears to be two ways of converting a linked-list to a
# binary search tree. The first is to convert the linked-list to
# an array. This will make accesses easier, and allow us to
# recursively build the bst. Runtime O(N). Storage O(N).
# Another method could be to count the number of nodes in the
# list on the first pass, and then build tree by walking through
# the linked-list iteratively. Runtime O(N). Storage O(1).
# We will work with the first method.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def ListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return self.create_BST(array, 0, len(array)-1)
        
    def create_BST(self, array, left, right):
        if left > right:
            return
        if left == right:
            return TreeNode(array[left])
        mid = (left + right) / 2
        node = TreeNode(array[mid])
        node.left = self.create_BST(array, left, mid-1)
        node.right = self.create_BST(array, mid+1, right)
        return node
