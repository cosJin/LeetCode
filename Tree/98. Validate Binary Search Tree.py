# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #方法一：对二叉排序树进行中序看历，看是否是升序的，
        #有个小技巧是不需要保存所有的遍历结果，而只保存上一个
        # 即可，看当前数是否比上一个大。 时间复杂度 O(n)
        
        #方法二：递归判断，valide(..,min,max)递归，
        #max <- valid(left)
        #min <. valid(right)
        #判断max < root && min > root 时间复杂度 O(n)
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def inorder(self,root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        ########中序遍历时不需要保存所有数组  如下###############################
    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)
    def helper(self,root):
        if root is None:
            return Ture
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root 
        return self.helper(root.right)
        #########递归的方法：###################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        mini, maxi = float('-inf'), float('inf') 
        return self.isValid(root, mini, maxi)
    
    def isValid(self, root: TreeNode, mini: int, maxi: int) -> bool:
        if root is None:
            return True
        if mini >= root.val or maxi <= root.val:
            return False
        return self.isValid(root.left, mini, root.val) and self.isValid(root.right, root.val, maxi)
