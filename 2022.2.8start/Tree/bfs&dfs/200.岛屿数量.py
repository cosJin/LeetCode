#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
from curses.ascii import SO


# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         res = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j]=='1':
#                     queue = set()
#                     queue.add((i,j))
#                     while len(queue)>0:
#                         queue=list(queue)
#                         m,n = queue.pop(0)
#                         queue=set(queue)
#                         grid[m][n] = '0'
#                         if n!=len(grid[0])-1 and grid[m][n+1] == '1':
#                             queue.add((m,n+1))
#                         if m!=len(grid)-1 and grid[m+1][n] == '1':
#                             queue.add((m+1,n))
#                         if n!=0 and grid[m][n-1] == '1':
#                             queue.add((m,n-1))
#                         if m!=0 and grid[m-1][n] == '1':
#                             queue.add((m-1,n))
#                     res +=1
#         return res

#和更好版本区别是，我的放进队列的时候不置零，会导致有的点会需要放入多次，则需要去重
#而下面版本则是放入队列之前就置零，下次判断需要放进去的点的时候就不会重复放入了
from collections import deque                
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        rows = len(grid)
        if not grid or not rows:
            return 0
        cols = len(grid[0])
        num_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    num_islands += 1
                    grid[r][c] = '0'
                    q = deque([(r,c)])
                    while q:
                        print(q)
                        i, j = q.popleft()
                        if i-1 >= 0 and grid[i-1][j] == '1':   
                            q.append((i-1,j))
                            grid[i-1][j] = '0'
                        if i+1 < rows and grid[i+1][j] == '1':
                            q.append((i+1,j))
                            grid[i+1][j] = '0'
                        if j-1 >= 0 and grid[i][j-1] == '1':
                            q.append((i,j-1))
                            grid[i][j-1] = '0'
                        if j+1 < cols and grid[i][j+1] == '1':
                            q.append((i,j+1))
                            grid[i][j+1] = '0'
        return num_islands
                        

# @lc code=end

print(Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]

))
