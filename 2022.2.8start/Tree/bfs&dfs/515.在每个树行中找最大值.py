#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:return []
        queue = [[root]]
        res = []
        for lv in queue:
            if lv != []:
                a = [n.val for n in lv]
                queue.append([])
                res.append(max(a))
                for nd in lv:

                    if nd.left is not None: queue[-1].append(nd.left)
                    if nd.right is not None: queue[-1].append(nd.right)
        return res
# @lc code=end

