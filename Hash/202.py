class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = {}
        sum = 0
        while 1:
            while n != 0:
                m = int(n%10)
                n = int(n/10)
                sum += m*m
            if sum not in result.keys():
                result[sum]=1
                n = sum
                sum = 0
                if n == 1:
                    return True
            else:return False
test = Solution()
print(test.isHappy(9))
        

