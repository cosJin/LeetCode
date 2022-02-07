# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            if p.val == q.val:return self.isSameTree(p.right,q.right) and self.isSameTree(q.left,p.left)
            else:return False
        elif not p and not q:
            return True
        else: return False
test = Solution()
a = TreeNode([0,-5])
b = TreeNode([0,-8])
print(test.isSameTree(a,b))