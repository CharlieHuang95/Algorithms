# An interval tree uses O(nlogn) space to save information about an array,
# so that the specific property (max/min) about the array can be retrieved
# in O(logn) time

import sys

class IntervalTree:
    def __init__(self, func, array):
        if func == max:
            self.func = max
            self.placeholder = -sys.maxint
        elif func == min:
            self.func = min
            self.placeholder = sys.maxint
        size = 1
        length = len(array)
        while length > 0:
            size += 1
            length /= 2
        self.tree = [self.placeholder] * 2 ** size
        self.size = 2 ** (size - 1)
        start = 2 ** (size -1)
        self.tree[start : start + len(array)] = array
        for x in xrange(start - 1, 0, -1):
            self.tree[x] = func(self.tree[2*x], self.tree[2*x + 1])

    def get_helper(self, index, left, right, desired_left, desired_right):
        if desired_left > right or desired_right < left:
            return
        if left == desired_left and right == desired_right:
            return self.tree[index]
        mid = (left + right) / 2
        l = self.placeholder
        r = self.placeholder
        if left <= desired_left <= mid:
            l = self.get_helper(2 * index, left, mid, desired_left, min(mid, desired_right))
        if mid + 1 <= desired_right <= right:
            r = self.get_helper(2 * index + 1, mid + 1, right, max(mid + 1, desired_left), desired_right)
        return self.func(l, r)

    def get(self, start, end):
        return self.get_helper(1, 0, self.size-1, start, end)

    def __str__(self):
        return str(self.tree)
   
if __name__=="__main__":
   interval_tree = IntervalTree(min, [9,4,2,7,6,1,8,4])
   assert interval_tree.get(0, 1) == 4
   assert interval_tree.get(0, 2) == 2
   assert interval_tree.get(0, 7) == 1
   interval_tree = IntervalTree(max, [9,4,2,7,6,1,8,4])
   assert interval_tree.get(0, 1) == 9
   assert interval_tree.get(1, 2) == 4
   assert interval_tree.get(1, 7) == 8
