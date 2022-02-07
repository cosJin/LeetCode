class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:return "1"
        result = ""
        result = self.sayLine("1")
        while n-2>0:
            result = self.sayLine(result)
            n-=1
        return result
    def sayLine(self,line):
        line+="0"
        count = 0
        number = line[0]
        result = ""
        for num in line:
            if number == num:count+=1
            else:
                result+=str(count)+str(number)
                count = 1
                number = num
        return result
test = Solution()
print(test.countAndSay(5))

