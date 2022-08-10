#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:return 0
        prices.append(0)
        profit = 0
        have = 0
        pr = 0
        for n,i in enumerate(prices[:-1]):
            if prices[n+1]<i and have == 1:
                profit += i-pr
                have = 0
            elif prices[n+1]>i and have == 0:
                pr = i
                have = 1
        return profit
# @lc code=end

print(Solution().maxProfit([1,2,3,4,5]))