class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
       #调函数
       # 暴力循环n 乘以x
       # 分治：分n为奇数还是偶数   偶数：计算 x，n/2  然后y*y 奇数：先计算x/2  再y*y*x  O(logn)   
        if not n:       # n == 0 的情况
            return 1
        if n < 0:     #此处要注意考虑情况！！
            return 1 / self.myPow(x,-n)
        if n % 2:       #用 % 判断奇数还是偶数
            return x*self.myPow(x,n-1)    # 奇数和 1 的情况都包含在这里面 
        return self.myPow(x*x,n/2)      