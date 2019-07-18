# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #方法一，寻找路径，寻找重合的地方。
        #方法二：Recursion： findPorQ(root,P,Q):找到谁就返回谁
        if (root is None or root == p or root == q):return root
        inleft == lowestCommonAncestor(self.left,p,q)
        inright == lowestCommonAncestor(self.right,p,q)
        return inleft is None ? right : right is None ? left : root
