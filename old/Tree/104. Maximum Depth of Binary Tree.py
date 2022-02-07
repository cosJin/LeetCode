# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
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
        #方法一：递归，取左右节点最大的，加根节点1 就是最深层数
        if not root : return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))  #相当于DFS

#DFS 每次遍历节点判断是否是叶子节点，如果是叶子节点就更新最深最浅层。  O(n)

#BFS   我的方法就相当于广度优先，就是看是不是叶子节点  O(n)


