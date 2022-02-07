# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.val > root.val and p.val > root.val:
            lca = self.lowestCommonAncestor(root.right,p,q)
        elif q.val < root.val and p.val < root.val:
            lca = self.lowestCommonAncestor(root.left,p,q)
        else:lca = root
        return lca

        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:return root