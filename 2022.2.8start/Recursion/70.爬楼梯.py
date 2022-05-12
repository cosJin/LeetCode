#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1 or n == 0: return 1
        # else :
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)
        if n == 0 or n == 1:return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(n+1)[2:]:
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        
# @lc code=end
print(Solution().climbStairs(2))
