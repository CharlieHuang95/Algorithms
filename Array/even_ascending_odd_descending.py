# Given an array of numbers, sort it so that the beginning portion has
# odd numbers in descending order, and the end portion has even numbers
# in ascending order.

# We can use two-pointer swapping to move all odd numbers to first half,
# and even numbers of second half.

def sort_even_odd(array):
    p1 = 0
    p2 = len(array)-1
    num_odds = 0
    while p1 < p2:
        while p1 < p2 and array[p1] % 2 == 1:
            p1 += 1
            num_odds += 1
        while p1 < p2 and array[p2] % 2 == 0:
            p2 -= 1
        if p1 < p2:
            array[p1], array[p2] = array[p2], array[p1]
    # At this point, p1 and p2 are equal and should be pointing to
    # the edge. Make sure that p1 does not dip below 0.
    if array[p1] % 2 == 1:
        boundary = p1
    else:
        boundary = max(p1 - 1, 0)
    array[:boundary+1] = sorted(array[:boundary+1], reverse=True)
    array[boundary+1:] = sorted(array[boundary+1:])
    return array

if __name__=="__main__":
    # General cases
    assert sort_even_odd([3,6,2,7,5,9,5]) == [9,7,5,5,3,2,6]
    assert sort_even_odd([1,2,3,4,5]) == [5,3,1,2,4]
    # All evens
    assert sort_even_odd([2,4,6,8]) == [2,4,6,8]
    # All odds
    assert sort_even_odd([3,5,7]) == [7,5,3]
