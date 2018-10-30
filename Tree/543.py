# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = 0
        if root is None:return 0
        if not root.left and not root.right: return 0
        longestFromNode = self.maxDepth(root.left) + self.maxDepth(root.right)
        longest = max(longest,longestFromNode,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return longest
        
    def maxDepth(self,root):
        if root is None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1

    # def maxDepth(self,root):
    #     if root is None:return 0
    #     maxDepth = 1
    #     next = []
    #     if root.left or root.right:
    #         next = [root.left,root.right]
    #     while next:
    #         now = next
    #         next = []
    #         for node in now:
    #             if node is not None:
    #                 if node.left or node.right:
    #                     next.append(node.left)
    #                     next.append(node.right)
    #         maxDepth += 1
    #     return maxDepth
