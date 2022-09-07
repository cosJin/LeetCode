#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        self.root={}
        self.end_of_word = "#"


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char,{}) 
            #如果char存在于node字典中，则返回node[char],不存在则返回{},同时node一层一层的深入
        node[self.end_of_word]=self.end_of_word  #增加一个end key标记词尾
        


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:return False
            node = node[char]
        return self.end_of_word in node  #到word的最后一个char后也要看这里是不是有词尾标记


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:return False
            node = node[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

