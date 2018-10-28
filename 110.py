# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:return True
        elif root.left is None and root.right is None:return True
        else:
            if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
                if self.isBalanced(root.left) and self.isBalanced(root.right):
                    return True
            return False

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        deepth = 1
        now = root
        next = []
        if root.left or root.right: next = [root.left,root.right]
        while next:
            now = next
            next = []
            deepth += 1
            for tree in now:
                if tree is not None:
                    if tree.left or tree.right:
                        next.append(tree.left)
                        next.append(tree.right)
        return deepth