class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        result = 0
        for i in range(len(s)-2):
            if s[i:i+2] in dic:
                result += dic[s[i:i+2]]
                result -= dic[s[i+1:i+2]]
            else:result += dic[s[i]]
        if s[-2:] in dic:
            result += dic[s[-2:]]
        else: result += dic[s[-1]]+dic[s[-2]]
        return result
test = Solution()
print(test.romanToInt("MCMXCIV"))

