# Merge sort works by recursively breaking down the array into smaller chunks
# (subproblems) until a subproblem consists of sorting individual elements.
# This is the base case. Since it is considered sorted, it will return.
# The solutions to the subproblems are then combined with a helper routine
# (merge) which merges two sorted arrays together. This can be run in O(n)
# time with a simple two-pointer approach.

import random

def merge(left, right):
    l = 0
    r = 0
    array = []
    while l < len(left) or r < len(right):
        if l >= len(left):
            array.extend(right[r:])
            break
        elif r >= len(right):
            array.extend(left[l:])
            break
        if left[l] > right[r]:
            array.append(right[r])
            r += 1
        else:
            array.append(left[l])
            l += 1
    return array

def merge_sort(array):
    # Base case is when the array is of size 0 (empty) or 1
    # Base case is already sorted so just return
    if len(array) < 2:
        return array
    # Divide it into a left and right side
    mid = len(array) / 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

if __name__=="__main__":
    for _ in xrange(10):
        array = []
        for _ in xrange(20):
            array.append(random.randrange(0, 100))
        assert merge_sort(array) == sorted(array)
    
