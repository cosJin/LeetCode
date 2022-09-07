#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for m,pp in enumerate(grid):
            for n,i in enumerate(pp):  
                if i == '1':
                    stack=[]
                    stack.append((m,n))
                    pp[n]='0'
                    while stack != []:
                        print(stack)
                        p=stack.pop()              
                        if p[0]!=0 and grid[p[0]-1][p[1]] == '1':
                            stack.append((p[0]-1,p[1]))
                            grid[p[0]-1][p[1]]='0'
                        if p[1]!=0 and grid[p[0]][p[1]-1] == '1':
                            stack.append((p[0],p[1]-1))
                            grid[p[0]][p[1]-1]='0'
                        if p[0]!=len(grid)-1 and grid[p[0]+1][p[1]] == '1':
                            stack.append((p[0]+1,p[1]))
                            grid[p[0]+1][p[1]]='0'
                        if p[1]!=len(grid[0])-1 and grid[p[0]][p[1]+1] == '1':
                            stack.append((p[0],p[1]+1))
                            grid[p[0]][p[1]+1]='0'
                        
                        if stack == []:    
                            res+=1
        return res
# @lc code=end
print(Solution().numIslands([
    ["1","1","1"],
    ["0","1","0"],
    ["0","1","0"]]))

