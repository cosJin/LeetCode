#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# class Solution2(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices)<=1:return 0
#         ps= []
#         m = prices[0]
#         ps.append(0)
#         for p in prices[1:]:
#             m = min(p,m)
#             profits = p-m
#             ps.append(profits)
#         return max(ps)  

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = float('inf')
        p = 0
        for i in prices:
            if i < mi:
                mi = i
            p = max(p,i-mi)
        return p
# @lc code=end

print(Solution().maxProfit([7,1,5,3,6,4]))