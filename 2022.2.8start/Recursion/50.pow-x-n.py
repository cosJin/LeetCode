#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:return 1
        elif n==1:return x

        if n>=0:
            if n%2==1:
                return x*self.myPow(x,n-1)
            else:
                return self.myPow(x*x,n/2) 
        else:
            return 1/self.myPow(x,-n)

# @lc code=end

