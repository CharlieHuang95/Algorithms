# Quicksort works by randomly selecting an element to be its pivot, and shifting
# smaller elements to its left side, and larger elements to its right side.
# At the end of all the shifting, the pivot should ultimately be in the correct
# location.

import random

def quick_sort_helper(array, left, right):
    if left >= right:
        return
    pivot = array[left]
    l = left + 1
    r = right
    while l < r:
        while l < r and array[l] < pivot:
            l += 1
        while l < r and array[r] > pivot:
            r -= 1
        if l < r:
            array[l], array[r] = array[r], array[l]
    if array[l] <= pivot:
        array[left], array[l] = array[l], array[left]
        boundary = l
    else:
        array[left], array[l-1] = array[l-1], array[left]
        boundary = l - 1
    quick_sort_helper(array, left, boundary - 1)
    quick_sort_helper(array, boundary + 1, right)

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)

if __name__=="__main__":
    for _ in xrange(10):
        array = []
        for _ in xrange(10):
            array.append(random.randrange(0, 100))
        quick_sort(array)
        assert sorted(array) == array
