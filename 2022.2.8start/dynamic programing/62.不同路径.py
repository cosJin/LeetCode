#
# @lc app=leetcode.cn id=62 lang=python
#
# [62] 不同路径
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0 for _ in range(n)] for _ in range(m)]
        # print(dp)
        for i in range(n):     ###还可以优化空间，不用存整个二维dp数组，只要存最近的一行即可。
            # print(i)
            dp[0][i]=1
        for i in range(m):
            dp[i][0]=1
        # print(dp)
        for r in range(m)[1:]:
            for c in range(n)[1:]:
                dp[r][c] = dp[r-1][c]+dp[r][c-1]
        return dp[-1][-1]
# @lc code=end
print(Solution().uniquePaths(3,2))
