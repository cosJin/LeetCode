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
        if n == 1:return 1 
        if n == 2:return 2
        a,b = 1,2
        while n>2:
            a,b = b,a+b
            n-=1
        return b

# @lc code=end

