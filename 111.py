# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:return 0
        levelNode = [root]
        nextNode = []
        level = 1
        while levelNode:
            for node in levelNode:
                if node is not None:
                    if node.right or node.left:
                        nextNode.append(node.left)
                        nextNode.append(node.right)
                    else:
                        return level
            levelNode = nextNode
            nextNode = []
            level += 1


