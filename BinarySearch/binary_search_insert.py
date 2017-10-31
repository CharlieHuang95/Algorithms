# Given an array and a value, return an array with the value
# inserted into the right location

# Probably worth nothing that this is useless because an insertion
# in a list takes O(n) time complexity, which negates the benefit
# of having binary search O(logn). This is a good exercise to consider
# the behaviour of binary search is a value is NOT found.

def binary_search_insert(array, value):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) / 2
        if array[mid] > value:
            right = mid - 1
        elif array[mid] < value:
            left = mid + 1
        else:
            return array.insert(mid, value)
    # At this point, the value is not found, and we have exited out of
    # the loop since left > right (more specifically left = right + 1)
    # This denotes the boundary: the value at left is smaller than our
    # target whereas the value on the right is bigger than our target.
    # The correct location to insert our value is left.
    array.insert(left, value);
    return array

if __name__=="__main__":
    array = [1,2,3,5,7,8]
    binary_search_insert(array, 0)
    assert array == [0,1,2,3,5,7,8]
    binary_search_insert(array, 9)
    assert array == [0,1,2,3,5,7,8,9]
    binary_search_insert(array, 4)
    assert array == [0,1,2,3,4,5,7,8,9]
    
