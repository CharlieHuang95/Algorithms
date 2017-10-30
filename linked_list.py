# Contains class definition of single linked list

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    def append_tail(self, val):
        cur = self
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)
    def append_head(self, val):
        val = Node(val)
        val.next = self
        return val
    def __str__(self):
        l = [self.val]
        cur = self.next
        while cur is not None:
            l.append(cur.val)
            cur = cur.next
        return "->".join(map(str,l))
