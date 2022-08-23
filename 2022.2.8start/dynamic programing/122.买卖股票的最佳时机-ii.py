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
        profits=0
        for n,i in enumerate(prices):
            if n>0 and i>prices[n-1]:
                profits += i-prices[n-1]
        return profits
            
# @lc code=end
print(Solution().maxProfit([7,1,5,3,6,4]))

