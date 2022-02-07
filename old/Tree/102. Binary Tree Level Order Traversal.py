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

# BFS方法：难点在于判断某层是不是结束了。batch process   O(n)
# DFS方法：遍历的时候记住深度，访问到每个数的时候填到相应的层数里就好
    def levelorder(self,root):   #广度优先方法
        if not root: return []
        result = []
        queue = collections.deque()  #python里面的双端队列。
        queue.append(root)

        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                current_level.append(node)
                if node.left:queue.append(node.left)  #因为当前的循环只循环当前层，所以就算这里队列
                if node.right:queue.append(node.right) #里加了下一层的节点也没关系
            result.append(current_level)
        return result
            
    def levelorder(self,root):   #深度优先方法
        if not root : return []
        self.result = []
        self._dfs(root,0)
        return self.result
    def _dfs(self,node,level):
        if not node:return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)
        self._dfs(node.left,level + 1)
        self._dfs(node.right,level + 1)

