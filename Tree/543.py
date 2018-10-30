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
        self.longest = 0
        def maxDepth(root):
            if root is None: return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.longest = max(self.longest,left + right)
            return max(left,right)+1
        maxDepth(root)
        return self.longest

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
