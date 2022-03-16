#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list2 is None:
            return list1
        elif list1 is None:
            return list2
        p1,p2 = list1,list2
        #res = p1 if p1.val<p2.val else p2
        head = res = ListNode()
        while p1 is not None or p2 is not None:           
        ####以上部分可以通过， p1 is not None and p2 is not None 简化掉
            if p1 is None:
                res.next = p2
                return head.next
            elif p2 is None:
                res.next = p1
                return head.next
            elif p1.val <= p2.val:
                res.next = p1
                p1 = p1.next
                res = res.next
            elif p1.val > p2.val:
                res.next = p2
                p2 = p2.next
                res = res.next
        # return head.next
        
# @lc code=end
# print(Solution().mergeTwoLists([1,3,4],[1,2,4]))
class Solution2(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        dummy = head
        while list1 and list2:
            if(list1.val<list2.val):
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        return head.next
                