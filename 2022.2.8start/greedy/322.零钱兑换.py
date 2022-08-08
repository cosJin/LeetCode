#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
# from cmath import inf

#一维动态规划，每个位置i 表示构成i元至少需要多少枚硬币，遍历i，对每个i处遍历所有硬币取最小值。
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0 :return 0
        dp = [0] * (amount+1)
        
        for i in range(len(dp))[1:]:
            tmp = []
            for coin in coins:
                if i>=coin:
                    tmp.append(dp[i-coin]+1)
            dp[i] = min(tmp) if tmp != [] else float('inf')
        return -1 if dp[-1] == float('inf') else dp[-1]

# @lc code=end

print(Solution().coinChange([1],1))
