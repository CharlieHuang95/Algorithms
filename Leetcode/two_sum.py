# Two Sum

# Given an array of integers, return the indices of the two numbers
# that add up to a chosen target.

# This question has a number of solutions and shows the trade-offs
# between space and time complexity. We show the trivial O(n^2) runtime
# and O(1) space solution, as well as the O(n) runtime, O(n) space
# solution.

class Solution(object):
    def twoSum_N2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            for j in xrange(len(nums)-1, i, -1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_N(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], i]
            hashmap[num] = i
        return []
