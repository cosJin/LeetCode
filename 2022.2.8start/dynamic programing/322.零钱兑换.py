#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:return 0
        if min(coins)>amount:return -1
        dp = [float('inf') for _ in range(amount+1)]
        for i in coins:
            if i<=amount:
                dp[i]=1
        print('now',dp)
        for i in range(len(dp))[1:]:
            tmp = []
            for c in coins:
                if i-c>0:
                    tmp.append(dp[i-c]+1)
            tmp.append(dp[i])
            dp[i] = min(tmp)
        return dp[-1] if dp[-1]!=float('inf') else -1


# @lc code=end

print(Solution().coinChange([1,32],2))
