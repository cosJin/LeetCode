# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return head
        elif head.next is None: return head
        cur,nex = head,head.next
        a = nex
        while nex.next is not None and nex.next.next is not None:
            cur.next,nex.next,cur,nex = nex.next.next,cur,nex.next,nex.next.next
        cur.next,nex.next = nex.next,cur
        return a
        
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next 
            pre = a 
        return self.next

        
