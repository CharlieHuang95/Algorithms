# Given an array and a target, perform binary search to find it

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while (left <= right):
        mid = (left + right) / 2
        if array[mid] > target:
            right == mid - 1
        elif array[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

if __name__=="__main__":
    array = range(10)
    for x in xrange(10):
        assert binary_search(array, x) == x
    assert binary_search(array, -1) == -1
