#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root is not None:
            for node in root.children:
                res += self.postorder(node)
            res.append(root.val)
        return res
# @lc code=end

