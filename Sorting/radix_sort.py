# Radix sort works by sorting elements lexicographically

import random

def num_digits(num):
    length = 0
    while num > 0:
        num /= 10
        length += 1
    return length

def get_digit(num, index):
    return (num / 10 ** index) % 10

def radix_sort_int(array):
    buckets = [[] for _ in xrange(10)]
    # Find the longest length
    longest_length = 0
    for num in array:
        longest_length = max(longest_length, num_digits(num))
    for x in xrange(longest_length):
        for num in array:
            buckets[get_digit(num, x)].append(num)
        # Combine buckets
        array = []
        for bucket in buckets:
            array.extend(bucket)
        buckets = [[] for _ in xrange(10)]
    return array  

def radix_sort(array):
    if not array:
        return []
    if type(array[0]) is int:
        return radix_sort_int(array)
    
if __name__=="__main__":
    for _ in xrange(10):
        array = []
        for _ in xrange(10):
            array.append(random.randrange(0, 100))
        assert sorted(array) == radix_sort(array)
