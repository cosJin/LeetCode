# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        def path(root,parentPath):
            if root is None:return None
            if not root.left and not root.right:
                result.append(parentPath+str(root.val))
            if root.left:
                path(root.left,parentPath+str(root.val)+"->")
            if root.right:
                path(root.right,parentPath+str(root.val)+"->")
        path(root,"")
        return result

            
class Solution2:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.allPath(root,[])

    def allPath(self,tree,parentPath):
        pathList = []
        if tree.left is None and tree.right is None:
            path = parentPath+[tree.val]   
            # path = parentPath.append(tree.val)   #这样就不可以运行，因为就改变了传入的参数，所以不要轻易改变传入参数。   
            pathList.append(path)          
        if tree.left:
            pathList += self.allPath(tree.left,parentPath+[tree.val])
        if tree.right:
            pathList += self.allPath(tree.right,parentPath+[tree.val])
        return pathList