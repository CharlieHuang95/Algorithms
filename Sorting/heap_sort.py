# Heap-sort works by adding all elements to a (min) heap, and iteratively
# popping the smallest elements onto a sorted array

# Has O(nlogn) runtime. This algorithm can be effective when we only require
# a fraction of the sorted array. For example, it can obtain the smallest
# m/n elements in O(n+mlogn) time, an improvement to the O(nlogn) normally
# required to fully sort an array. This is achieved because the creation of
# a heap is O(n), and only m elements need to be popped from the heap.

import heapq
import random

def heap_sort(array):
    # It is important to note that heapify modifies the original structure
    # of the array
    temp = array[:]
    heapq.heapify(temp)
    sorted_array = []
    while temp:
        sorted_array.append(heapq.heappop(temp));
    return sorted_array

if __name__=="__main__":
    array = []
    for _ in xrange(10):
        array.append(random.randrange(0, 100))
    assert heap_sort(array) == sorted(array)
