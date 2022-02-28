# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#比较好的方法
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:return head
        if head.next is None:return head
        
        i,j = head,head.next
        res = head.next
        while i.next.next and j.next.next:  #如果i.next.next is None,则不会执行j.next.next,所以不会报错
            j.next,i.next,i,j = i,j.next.next,j.next,j.next.next
        i.next,j.next = j.next,i
        return res
        
#2.28日自己想的，有点繁琐
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:return head
        elif head.next is None:return head
        res = head.next
        if head.next.next is None:
            head.next.next,head.next = head,None
            return res
        i,j,k = head,head.next,head.next.next
        while k:
            j.next,i.next,i,j = i,(k.next if k.next else k),k,(k.next if k.next else None)
            k =  j.next if j else None
        if j:
            j.next = i
            i.next = None
        return res


  #discuss 中的迭代法      
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
