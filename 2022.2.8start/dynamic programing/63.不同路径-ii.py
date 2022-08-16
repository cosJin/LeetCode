#
# @lc app=leetcode.cn id=63 lang=python
#
# [63] 不同路径 II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:return 0
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            if obstacleGrid[i][0] != 1:dp[i][0]=1
            else:
                break
        for j in range(c):
            if obstacleGrid[0][j] != 1:dp[0][j]=1
            else:
                break

        for i in range(r)[1:]:
            for j in range(c)[1:]:
                if obstacleGrid[i][j]!=1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# @lc code=end

print(Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))