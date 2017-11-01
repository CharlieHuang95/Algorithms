# Insertion sort works by iteratively expanding a frontier of sorted
# values. This involves finding the correct position to place the next
# value.

import random

def insertion_sort(array):
    for x in xrange(1, len(array)):
        element = array[x]
        for y in xrange(0, x):
            if array[y] >= element:
                array.pop(x)
                array.insert(y, element)
                break

if __name__=="__main__":
    array = []
    for _ in xrange(10):
        array.append(random.randrange(0, 100))
    insertion_sort(array)
    assert array == sorted(array)
