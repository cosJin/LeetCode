# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            head.next.next = head
            head = head.next
            head.next.next = None
            return head
        elif head.next.next is not None:
            i = head.next
            j = head.next.next
            head.next = None
            while j is not None:
                i.next = head
                head = i
                i = j
                j = j.next
            i.next = head
            head = i
            return head
#简洁的写法
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None  #引入一个None放在head之前，可以方便的讲head指向none
        while cur:  #比较巧妙
            cur.next,cur,prev = prev,cur.next, cur   #利用python同时计算的特性，不引入额外变量的情况下调转指针
        return prev

#简洁的写法
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None  #引入一个None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev



        