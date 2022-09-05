#
# @lc app=leetcode.cn id=714 lang=python
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # dp[i][0] 表示当前手里不持有股票的情况下 的 最大收益
        # dp[i][1] 表示当前手里 持有股票的情况下 的 最大收益
        dp=[[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][1]=-prices[0]
        for i in range(len(prices))[1:]:
            dp[i][0]=max(dp[i-1][1]+prices[i]-fee,dp[i-1][0])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
# @lc code=end

