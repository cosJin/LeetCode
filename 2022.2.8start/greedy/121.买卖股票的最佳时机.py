#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi = float('inf')
        res = []
        p = float('-inf')
        for n,i in enumerate(prices):
            if i < mi:
                mi = i
            p = max(p,i-mi)

        
        return p



# @lc code=end

print(Solution().maxProfit([7,1,5,3,6,4]))