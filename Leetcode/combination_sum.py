# Combination Sum

# Given an array of positive integers, and a target, find all
# combinations of these integers that sum up to the target.

# This problem can be solved using recursion. At each node, we keep
# track of the current total, and we evaluate whether the current
# selection sum up to the target. If the current total is less than
# the target, we attempt to select more elements to reach the target.
# If the current sum exceeds the target (we are only given positive
# values) or if there are no more values to select, we must backtrack.
# We can also optimize by removing values at the beginning that are
# larger than the target.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(path, total, index):
            if total == target:
                solution.append(path[:])
                return
            if total > target:
                return
            for x in xrange(index, len(candidates)):
                path.append(candidates[x])
                dfs(path, total + candidates[x], x)
                path.pop()
                
        candidates = sorted(candidates)
        for x in xrange(len(candidates)):
            if candidates[x] > target:
                candidates = candidates[:x]
                break
        candidates = candidates[::-1]
        solution = []    
        dfs([], 0, 0)
        return solution
