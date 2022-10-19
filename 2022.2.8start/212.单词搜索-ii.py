#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#

# @lc code=start
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        

        def helper(word1,board1,m,n):
            if word1 == []:return True
            if m-1 >= 0 and board1[m-1][n] == word1[0]:
                board1[m-1][n] = 0
                b = board1[:]
                return helper(word1[1:],b,m-1,n)
            if n-1 >= 0 and board1[m][n-1] == word1[0]:
                board1[m][n-1] = 0
                b = board1[:]
                return helper(word1[1:],b,m,n-1)
            if m+1 <=len(board1)-1 and board1[m+1][n] == word1[0]:
                board[m+1][n] = 0
                b = board1[:]
                return helper(word1[1:],b,m-1,n)
            if n+1 <=len(board1[0])-1 and board1[m][n+1] == word1[0]:
                board[m][n+1] = 0
                b = board1[:]
                return helper(word1[1:],b,m,n+1)

        res = []
        for word in words:
            tmp = board[:]
            for mm in range(len(tmp)):
                for nn in range(len(tmp[0])):
                    if tmp[mm][nn] == word[0]:
                        if helper(word,tmp,mm,nn):
                            res.append(word)
                            continue
        return res
# @lc code=end

