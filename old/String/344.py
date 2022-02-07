class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)):
            result+=s[-i]
        return result
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
test = Solution()
print(test.reverseString2("Hello World!"))

