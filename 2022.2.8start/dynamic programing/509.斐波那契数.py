#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:return n
        else:
            a,b = 0,1
            while n>=2:
                a,b = b,a+b
                n-=1
        return b
            
        
# @lc code=end

