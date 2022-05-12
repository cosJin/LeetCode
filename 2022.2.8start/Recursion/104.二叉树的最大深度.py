#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(nodes,n):
        #     tmp=[]
        #     if nodes == [None]*len(nodes):return n
        #     else:
        #         for node in nodes:
        #             if node is not None:
        #                 tmp.append(node.left)
        #                 tmp.append(node.right)
        #     return helper(tmp,n+1)
        # return helper([root],0)
                
            tmp=[]
            for node in nodes:
                if node is not None:
                    tmp.append(node.left)
                    tmp.append(node.right)
            if tmp == []: return n
            return helper(tmp,n+1)
        return helper([root],0)
        
# @lc code=end

