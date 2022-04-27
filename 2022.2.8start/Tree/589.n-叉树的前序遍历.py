#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root is not None:
            res.append(root.val)
            for node in root.children:
                res += self.preorder(node)
        return res
# @lc code=end

