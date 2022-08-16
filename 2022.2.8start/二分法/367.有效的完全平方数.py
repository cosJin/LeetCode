#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:return True
        l,h = 0,int(num/2)
        while l<=h:
            t = int((l+h)/2)
            if t**2==num:return True
            elif t**2>num and (t-1)**2<num:return False
            elif t**2<num and (t+1)**2>num:return False
            elif t**2>num:h = t-1
            elif t**2<num:l = t+1
# @lc code=end
print(Solution().isPerfectSquare(1))

