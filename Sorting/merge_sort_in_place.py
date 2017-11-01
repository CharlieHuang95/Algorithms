import random

def merge(array, left, mid, right):
    # Create a copy here, memory requirement is only as large as
    # the array
    temp = array[:]
    p = left
    l = left
    r = mid + 1
    while l < mid + 1 or r < right + 1:
        if l >= mid + 1:
            array[p:right + 1] = temp[r:right + 1]
            break
        elif r >= right + 1:
            array[p:right + 1] = temp[l:mid + 1]
            break
        if temp[l] > temp[r]:
            array[p] = temp[r]
            r += 1
            p += 1
        else:
            array[p] = temp[l]
            l += 1
            p += 1
    return array

def merge_sort_helper(array, left, right):
    # Base case is when the array is of size 0 (empty) or 1
    # Base case is already sorted so just return
    if left >= right:
        return
    # Divide it into a left and right side
    mid = (left + right) / 2
    merge_sort_helper(array, left, mid)
    merge_sort_helper(array, mid + 1, right)
    merge(array, left, mid, right)

def merge_sort(array):
    merge_sort_helper(array, 0, len(array)-1);

if __name__=="__main__":
    for _ in xrange(10):
        array = []
        for _ in xrange(20):
            array.append(random.randrange(0, 100))
        merge_sort(array)
        assert sorted(array) == array
    
