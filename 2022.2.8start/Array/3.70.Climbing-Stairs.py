class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        :type n: int
        :rtype: int
        """
        # if n == 1:return 1
        # elif n == 2:return 2
        # else:
        #     a = 1
        #     b = 2
        #     res = 0
        #     t = 3
        #     while t<=n:
        #         res = a+b
        #         a,b = b,res
        #         t+=1
        #     return res

        if n == 1:return 1
        elif n == 2:return 2
        else:
            dp = [1 for _ in range(n+1)]
            for i in range(n+1)[2:]:
                dp[i] = dp[i-1] + dp[i-2]
            return dp[-1]

print(Solution().climbStairs(5))

