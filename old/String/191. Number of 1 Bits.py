class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #方法一：先模2，然后右移一位
        #x = x & (x-1) 去掉最右侧的 1 ,while(x!=0)即可
        i = 0
        while n != 0:
            n = n & (n-1)
            i+=1
        return i