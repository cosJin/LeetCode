#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(nodes,n):
            tmp=[]
            for node in nodes:
                if node is not None:
                    if node.left is None and node.right is None:
                        return n+1
                    else:
                        tmp.append(node.left)
                        tmp.append(node.right)
            if tmp == []: return n
            return helper(tmp,n+1)
        return helper([root],0)
        

# @lc code=end

