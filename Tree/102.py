# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        result = []
        levelresult,nextlevel = self.level([root])
        result.append(levelresult)
        while nextlevel:
            levelresult,nextlevel = self.level(nextlevel)
            result.append(levelresult)
        return result
    def level(self,rootList):
        levelResult = []
        nextLevel = []
        for root in rootList:
            if root is not None:
                levelResult.append(root.val)
                if root.left or root.right:
                    nextLevel.append(root.left)
                    nextLevel.append(root.right)
        return [levelResult,nextLevel]


