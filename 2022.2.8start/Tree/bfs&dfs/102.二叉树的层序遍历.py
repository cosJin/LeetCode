#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        tree = [[root]]
        res = []
        for level in tree:
            if level == []:return res
            res.append([])
            tree.append([])
            for node in level:
                if node is not None:
                    res[-1].append(node.val)
                    if node.left is not None:
                        tree[-1].append(node.left)
                    if node.right is not None:
                        tree[-1].append(node.right)
                        
class Solution:   #不用像上面那么巧妙，直接定义一个当前，一个待遍历节点就行，然后将结果存一个。
    def levelOrder(self, root):
        if root is None:return []
        now,nxt = [root],[]
        res = [] 
        while now != []:
            res.append([])
            for node in now:
                res[-1].append(node.val)
                if node.left is not None:nxt.append(node.left)
                if node.right is not None:nxt.append(node.right)
            now = nxt[:]  #浅拷贝 注意
            nxt = []
        return res




# @lc code=end

