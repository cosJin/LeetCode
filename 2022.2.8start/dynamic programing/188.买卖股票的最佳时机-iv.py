#
# @lc app=leetcode.cn id=188 lang=python
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:return 0
        l = [[0 for _ in range(len(prices))] for _ in range(k+1)]   
        #l表示在当前处卖出，所能得到的最大收益,需要判断在上个位置的全局最佳加上当前天和上一天的价差，和上一天不卖今天卖的收益哪个大
        g = [[0 for _ in range(len(prices))] for _ in range(k+1)]
        #g表示全局最大收益，需要判断当前卖出的收益大，还是当前不操作的收益大
        for j in range(k+1)[1:]:
            for i in range(len(prices))[1:]:
                diff = prices[i] - prices[i-1]
                l[j][i] = max(g[j-1][i-1]+max(diff,0),l[j][i-1]+diff)
                g[j][i] = max(l[j][i],g[j][i-1])
        return g[-1][-1]
# @lc code=end
print(Solution().maxProfit(2,[2,4,1]))

