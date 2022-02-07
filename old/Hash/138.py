# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        node_map = {}
        if head is None: return None
        new_head = RandomListNode(head.label)
        node_map.update({head:new_head})
        pNew = new_head
        p = head.next
        while (p != None):
            newNode = RandomListNode(p.label)
            pNew.next = newNode
            node_map.update({p:newNode})
            p = p.next
            pNew = newNode
        p = head
        pNew = new_head
        while p is not None:
            if p.random is not None:
                pNew.random = node_map[p.random]
                # pNew.random = p.random   #这样就错了。p.random是原始列表中的节点，需要利用map映射找到原始列表中节点对应的新列表的节点才可以。
            p = p.next
            pNew = pNew.next
        return new_head
            


   