#
# @lc app=leetcode.cn id=309 lang=python
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # dp[i][0] 表示当前手里不持有股票的情况下 的 最大收益
        # dp[i][1] 表示当前手里 持有股票的情况下 的 最大收益
        dp=[[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][1]=-prices[0]
        for i in range(len(prices))[1:]:
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1]=max(dp[i-2][0]-prices[i],dp[i-1][1])
        return dp[-1][0]
# @lc code=end

