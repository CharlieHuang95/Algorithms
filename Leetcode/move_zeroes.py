# Move Zeroes

# Given an array of 0s and 1s, move the ones to the beginning.

# This problem can be solved by manipulating pointers, or by
# counting the number of ones, and re-writing the entire array.
# We will use two pointers in our solution.

class Solution(object):
    def moveZeroes(self, nums):
        p1 = 0
        p2 = 0
        while p2 < len(nums):
            while p2 < len(nums) and nums[p2] == 0:
                p2 += 1
            if p2 < len(nums):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 += 1
