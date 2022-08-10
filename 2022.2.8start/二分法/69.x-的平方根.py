#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根 
#

# @lc code=start
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==1:return 1
        l,h = 0,int(x/2)
        while l <= h:
            t = int((l+h)/2)
            print(l,h,t)
            if t*t==x:return t
            elif t*t > x:
                h = t-1
            else:
                l = t+1
        return l-1 if l*l>x else h
class Solution(object):  #二分法
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0; h = x
        while l <= h:
            mid = l + (h-l)//2
            if mid*mid <= x and (mid+1)*(mid+1)>x:  #如果一样 则返回
                return mid
            elif mid*mid > x:   #如果大了，h=mid-1 
                h = mid - 1
            else:
                l = mid + 1    #如果小了，l = mid+1
        return l
            
# @lc code=end

print(Solution().mySqrt(8))
