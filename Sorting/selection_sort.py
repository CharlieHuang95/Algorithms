# Selection sort works by iteratively moving the smallest element to
# its final sorted position. On each iteration, its sorted 'frontier'
# is incremented once.

# Selection sort has O(n^2) runtime. One use case where it is not severely
# lacking is in updating an already sorted array with relatively few entry.

import random

def selection_sort(array):
    for x in xrange(0, len(array) - 1):
        # Find the index of the minimum
        minimum = array[x]
        index = x
        for y in xrange(x + 1, len(array)):
            if minimum > array[y]:
                index = y
                minimum = array[y]
        array[x], array[index] = array[index], array[x]

if __name__=="__main__":
    array = []
    for _ in xrange(10):
        array.append(random.randrange(0, 100))
    selection_sort(array)
    assert sorted(array) == array
    
