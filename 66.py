class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        diglen=len(digits)-1
        if digits[diglen]!=9:
            digits[diglen]+=1
            return digits
        elif digits[len(digits)-1]==9:
            if(len(digits)==1):
                digits.insert(0,1)
            digits[diglen]=0
            return(self.plusOne(digits[0:-1])+[0])
hello = Solution()
print(hello.plusOne([9]))