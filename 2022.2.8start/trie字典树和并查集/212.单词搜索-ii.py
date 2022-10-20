#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#
from matplotlib import collections


# @lc code=start
class Solution(object):

    def _dfs(self,board,i,j,cur_word,cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if self.END_OF_WORD in cur_dict:
                self.result.add(cur_word)
            tmp,board[i][j] = board[i][j],'@'
            for k in range(4):
                x,y = i + self.dx[k],j + self.dy[k]
                if 0 <= x<self.m and 0<=y <self.n and board[x][y]!='@' and board[x][y] in cur_dict:
                    self._dfs(board,x,y,cur_word,cur_dict)
            board[i][j] = tmp

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.dx = [-1,1,0,0]
        self.dy = [0,0,-1,1]
        self.END_OF_WORD = "#"

        if not board or not board[0]:return []
        if not words:return []
        self.result = set()

        #构建ｔｒｉｅ
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,collections.defaultdict())
            node[self.END_OF_WORD] = self.END_OF_WORD

        self.m,self.n = len(board),len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board,i,j,"",root)
        return list(self.result)
# @lc code=end

