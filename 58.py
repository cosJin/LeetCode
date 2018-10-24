class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":return 0
        elif len(s.split())==0:
            return 0
        else:return len(s.split()[-1])
test = Solution()
print(test.lengthOfLastWord("hello world "))