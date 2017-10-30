# Given the root of a Singly LL, reverse it

from linked_list import Node

def reverse(head):
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

def reverse_rec(head):
    def recursive(node, prev):
        if not node:
            return prev
        temp = node.next
        node.next = prev
        return recursive(temp, node)
    return recursive(head, None)
        

if __name__=="__main__":
    for func in [reverse, reverse_rec]:
        head = Node(1)
        head.append_tail(2)
        head.append_tail(3)
        assert str(head) == "1->2->3"
        head = func(head)
        assert str(head) == "3->2->1"
        head.append_tail(0)
        head = func(head)
        assert str(head) == "0->1->2->3"
        head = head.append_head(-1)
        head = func(head)
        assert str(head) == "3->2->1->0->-1"
    
