#
# @lc app=leetcode.cn id=141 lang=python
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = head
        f = head
        #while s is not None and f is not None:
        #  判断快指针不为零即可，则while中的判断可省略
        while f and f.next:
           # if f.next is None:
           #     return False
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
# @lc code=end

