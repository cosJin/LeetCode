class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}for _ in range(9)]
        col = [{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}for _ in range(9)]
        grid = [[{1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}for _ in range(3)]for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":continue
                else:
                    num = int(board[i][j])
                    if row[i][num] == 1 or col[j][num] == 1 or grid[int(i/3)][int(j/3)][num] == 1:return False
                    else: 
                        row[i][num] = 1
                        col[j][num] = 1
                        grid[int(i/3)][int(j/3)][num] = 1
        return True

test = Solution()
a = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
b = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(test.isValidSudoku( b ))