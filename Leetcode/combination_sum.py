# Combination Sum

# Given an array of integers, and a target, find all combinations
# of these integers that sum up to the target.

# This problem can be solved using recursion. At each node, we
# evaluate whether the current selection sum up to the target. We
# backtrack if it goes over the target (since we are only given
# positive values), or if there are no more values to select.
# We can also optimize by removing values that are larger than
# the desired sum.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(total, path, index):
            if total == target:
                solution.append(path[:])
                return
            if total > target:
                return
            for x in xrange(index, len(candidates)):
                path.append(candidates[x])
                dfs(total + candidates[x], path, x)
                path.pop()
                if total + candidates[x] > target:
                    break
        candidates = sorted(candidates)
        for x in xrange(len(candidates)):
            if candidates[x] > target:
                candidates = candidates[:x]
                break
        solution = []    
        dfs(0, [], 0)
        return solution
