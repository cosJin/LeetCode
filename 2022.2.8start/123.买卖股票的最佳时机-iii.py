#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        def submax(prices):
            mi = float('inf')
            p = 0
            for i in prices:
                if i < mi:
                    mi = i
                p = max(p,i-mi)
            return p
        ma = 0
        for n,i in enumerate(prices):
            a,b = prices[:n],prices[n:]
            ma = max(ma,submax(a)+submax(b))
        return ma

    def maxProfit(self, prices):
        
        if not prices:
            return 0 
        
        K = 2+1   #2为允许的最多交易次数
        n = len(prices)
        dp = [[0]*n for _ in range(K)]
       
        for k in range(1, K):   #1,2,3,...,K-1
            print(k)
            min_p = prices[0]
            for i in range(1, n):
                min_p = min(min_p, prices[i]-dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i]-min_p)
        return dp[-1][-1]
# @lc code=end

print(Solution().maxProfit([3,3,5,0,0,3,1,4]))