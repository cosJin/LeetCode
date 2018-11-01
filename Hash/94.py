# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:return None
        result+=self.inorderTraversal(root.left)
        result+=root.val
        result+=self.inorderTraversal(root.right)
        return result


