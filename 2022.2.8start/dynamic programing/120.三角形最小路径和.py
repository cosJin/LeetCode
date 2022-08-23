#
# @lc app=leetcode.cn id=120 lang=python
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp=[]
        for i in range(len(triangle)):
            dp.append([0 for _ in range(i+1)])
        dp[0][0] = triangle[0][0]
        for i in range(len(triangle))[1:]:
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j]+triangle[i][j]
                elif j==len(dp[i])-1:
                    dp[i][j] = dp[i-1][j-1]+triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
        return min(dp[-1])
# @lc code=end

print(Solution().minimumTotal( [[2],[3,4],[6,5,7],[4,1,8,3]]))