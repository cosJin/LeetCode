#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for m,pp in enumerate(board):
            for n,i in enumerate(pp):  
                if m==0 or m==len(board)-1 or n == 0 or n == len(board[0])-1:
                    if i == 'O':
                        stack=[]
                        stack.append((m,n))
                        pp[n]='B'
                        while stack != []:
                            p=stack.pop()              
                            if p[0]!=0 and board[p[0]-1][p[1]] == 'O':
                                stack.append((p[0]-1,p[1]))
                                board[p[0]-1][p[1]]='B'
                            if p[1]!=0 and board[p[0]][p[1]-1] == 'O':
                                stack.append((p[0],p[1]-1))
                                board[p[0]][p[1]-1]='B'
                            if p[0]!=len(board)-1 and board[p[0]+1][p[1]] == 'O':
                                stack.append((p[0]+1,p[1]))
                                board[p[0]+1][p[1]]='B'
                            if p[1]!=len(board[0])-1 and board[p[0]][p[1]+1] == 'O':
                                stack.append((p[0],p[1]+1))
                                board[p[0]][p[1]+1]='B'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':board[i][j]='X'
                elif board[i][j] == 'B':board[i][j]='O'
        return board

# @lc code=end

print(Solution().solve([
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]))