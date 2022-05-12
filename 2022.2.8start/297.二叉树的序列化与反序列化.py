#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        arr = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            arr.append(str(node.val) if node else 'null')
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
        while arr[-1] == 'null':
            arr.pop()
        
        return ','.join(arr)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        queue = list(map(lambda x: None if x=='null' else int(x), data.split(',')))
        Tree_queue = []
        root = None
        
        while queue:
            val = queue.pop(0)
            if not root:
                root = TreeNode(val)
                Tree_queue.append((root, 'left'))
                continue
            
            node, side = Tree_queue.pop(0)
            
            if side == 'left':
                if val is not None:
                    node.left = TreeNode(val)
                    Tree_queue.append((node.left, 'left'))
                Tree_queue.insert(0, (node, 'right'))
                
            
            elif side == 'right':
                if val is not None:
                    node.right = TreeNode(val)
                    Tree_queue.append((node.right, 'left'))
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

