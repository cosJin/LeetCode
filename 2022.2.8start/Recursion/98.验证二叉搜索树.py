#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # def helper(root,floor,tail):
        #     if root.left is None and root.right is None:
        #         return floor<root.val<tail
        #     elif root.right is None and root.left is not None : 
        #         return (root.left.val<root.val) and helper(root.left,floor,root.val) and floor<root.val<tail
        #     elif root.left is None and root.right is not None: 
        #         return (root.right.val>root.val) and helper(root.right,root.val,tail) and floor<root.val<tail
        #     else: 
        #         return helper(root.left,floor,root.val) and helper(root.right,root.val,tail) and (root.left.val < root.val) and (root.right.val > root.val) and floor <root.val<tail 
        # return helper(root,-999999999999,9999999999999)
        def helper(root,floor,tail):
            if root is None:return True
            else:return helper(root.left,floor,root.val) and helper(root.right,root.val,tail) and floor<root.val<tail
        return helper(root,-999999999999,9999999999999)
             
# @lc code=end

