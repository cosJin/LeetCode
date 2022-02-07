# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:return True
        return self.zzy(root.left) == self.yzz(root.right)

    def zzy(self,root):
        result = []
        if root is None: result.append(None)
        elif root.left != None or root.right != None:
            result.append(self.zzy(root.left))
            result.append(root.val)
            result.append(self.zzy(root.right))
        else:result.append(root.val)
        return result
    
    def yzz(self,root):
        result = []
        if root is None: result.append(None)
        elif root.left != None or root.right != None:
            result.append(self.yzz(root.right))
            result.append(root.val)
            result.append(self.yzz(root.left))
        else:result.append(root.val)
        return result