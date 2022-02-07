class Solution:
    def mySqrt(self, x: int) -> int:
        #方法一：二分查找
        #牛顿迭代法：可以通过xn+1 = xn - f(xn)/f'(xn)   x会趋向于y=0的根
        if x == 0 or x == 1: return x
        l ,r =1, x
        while l <= r:
            m = (l+r)/2
            if m == x/m:
                return m
            elif m > x/m:
                r = m - 1
            else:
                l = m + 1
            res = m 
        return res
    def mySqrt2(self, x):

        start, end = 0 ,x 
        
        while (start <= end):
            mid = start + (end - start)/2
            print(mid)
            if (mid+1)*(mid+1) > x and mid*mid <= x:
                return mid
            
            if mid*mid > x:
                end = mid-1
            else:
                start = mid + 1
        return mid
a = Solution()
print(a.mySqrt2(9))