# Permutations

# Given an array of numbers, generate a list of all possible
# permutations. We can assume that there are no duplicates.

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(path):
            if len(path) == len(nums):
                permutations.append(path[:])
                return
            for x in nums:
                if x in path:
                    continue
                path.append(x)
                dfs(path)
                path.pop()
        permutations = []
        dfs([])
        return permutations 
