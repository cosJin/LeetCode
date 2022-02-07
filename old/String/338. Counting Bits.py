class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #for i in range(num) 用191的方法分别统计1的个数
        #初始化一个count(n+1),count[i] = count[i&(i-1)] + 1,这样在算第i个数的1的个数时，可以利用前面已经算好的来求。
        count = [0] * (num+1)
        
        for i in range(num+1)[1:]:
            count[i] = count[i&(i-1)]+1
        return count
a = Solution()
print(a.countBits(8))
