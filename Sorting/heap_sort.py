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
