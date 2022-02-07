class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #1.相当于每个节点有卖和买两个子树，进行深度优先搜索 DFS    O(2^n)
        #2、贪心算法：只要后一天比今天高，则今天买进   O(n)
        #3、动态规划  O(n)
        res = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                res += (prices[i+1]-prices[i])
        return res