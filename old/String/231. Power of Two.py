class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #不停的除以2
        #取log2  看是否为int
        #位运算x & (x-1)  利用特性： 所有2的 n次方，都是只有一个1 
        return n != 0 and n&(n-1) == 0