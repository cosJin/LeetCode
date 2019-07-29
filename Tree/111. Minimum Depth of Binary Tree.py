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

        if(!root): return 0   #因为求最深的时候，空节点可以看0深度，不影响最大结果，
            #但是求最浅的时候，0深度就太小了，应该不看0深度的节点，所以下面两行排除了节点为空的情况
        if(!root.left): return 1 + minDepth(root.right) + 0  
        if(!root.right): return 1 + minDepth(root.left) + 0   #两行可以合并为一行，只要有个为空则就是1+left+right

        lefmin = minDepth(root.left)
        rigmin = minDepth(root.right)
        res = 1+min(lefmin,rigmin)
        return res

