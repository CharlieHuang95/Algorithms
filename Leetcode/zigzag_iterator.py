# Zig-Zag Iterator

# Given two arrays, create an iterator object that switches between the
# two array.

class zziter(object):
    def __init__(self, a, b):
        self.a = a[::-1]
        self.b = b[::-1]
        self.nextA = True
    def next(self):
        if not self.hasnext():
            return False
        if not self.a:
            return self.b.pop()
        if not self.b:
            return self.a.pop()
        if self.nextA:
            self.nextA = False
            return self.a.pop()
        else:
            self.nextA = True
            return self.b.pop()
    def hasnext(self):
        if not self.a and not self.b:
            return False
        return True

if __name__=="__main__":
    zzit = zziter([1,2,4,6],[3,5,6,7])
    array = [1,3,2,5,4,6,6,7]
    for num in array:
        assert num == zzit.next()
    zzit = zziter([],[1,2,3])
    array = [1,2,3]
    for num in array:
        assert num == zzit.next()
        
