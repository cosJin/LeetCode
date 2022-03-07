#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = head
        f = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                break
        else:
            return None
        while head != s:
            head = head.next
            s = s.next
        return head
#循环就是可以一直往前，看有没有重复，而检查重复可以首先想到set 和 dir
class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        visited = set()
        node = head
        
        while node != None:
            
            if node in visited:
                return node 
            
            visited.add(node)
            node = node.next 
            
        return node

        
# @lc code=end


