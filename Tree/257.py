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
            if root.right
                path(root.right,parentPath+str(root.val)+"->")
        path(root,"")
        return result

            
class Solution2:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        parentPath = []
        return self.allPath(root,parentPath)

    def allPath(self,tree,parentPath):
        pathList = []
        if tree.left is None and tree.right is None:
            path = parentPath.append(tree.val)   #[1,2,4]
            pathList.append(path)                #[[1,2,4]]
        if tree.left:
            parentPath.append(tree.val)
            pathList += self.allPath(tree.left,parentPath)
        if tree.right:
            parentPath.append(tree.val)
            pathList += self.allPath(tree.right,parentPath)
        return pathList