#
# @lc app=leetcode.cn id=25 lang=python
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
###
###
###
###  直接抄的答案，主要思路就是 每k个节点为一个单位，在单位内进行全翻转
###  这个思路其实在in pair翻转里面也可以用
###
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next
# @lc code=end

