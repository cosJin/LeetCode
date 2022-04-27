#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from xml.dom.minicompat import NodeList


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        final = []
        if root is None: return []
        else:
             final.append([root.val])
        def reprocess(node_list):
            if len(node_list) > 0:
                res=[]
                tmp = []
                for node in node_list:
                    if node is not None:
                        res.append(node.val)
                        tmp += node.children
                final.append(res)
                reprocess(tmp)
        reprocess(root.children)
        return final
        
# @lc code=end

