# Given the root of a Singly LL, reverse it

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

def reverse(head):
    # a -> b -> c -> d
    if not head:
        return
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

if __name__=="__main__":
    head = Node(1)
    head.append_tail(2)
    head.append_tail(3)
    assert str(head) == "1->2->3"
    head = reverse(head)
    assert str(head) == "3->2->1"
    head.append_tail(0)
    head = reverse(head)
    assert str(head) == "0->1->2->3"
    head = head.append_head(-1)
    head = reverse(head)
    assert str(head) == "3->2->1->0->-1"
    
