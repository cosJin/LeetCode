#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution2(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        t = 1
        res = 0
        for i in digits[::-1]:
            res += i * t
            t *= 10
        res += 1
        print(res)
        r = []
        while res>0:
            r.append(res%10)
            res/=10
        return r[::-1]
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        
        for i in range(len(digits)):
            if digits[i] == 9:               #如最后一位为9，则置零，
                digits[i] = 0
                if i == len(digits)-1:
                    digits.append(1)
            else:                              #知道遇到不是9的位，+1
                digits[i] += 1            
                return digits[::-1]
        return digits[::-1]
# @lc code=end

print(Solution().plusOne([1,2,3,4,9,9,9]))
