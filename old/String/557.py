class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for word in s.split():
            result.append(word[::-1])
        return ' '.join(result)
test = Solution()
print(test.reverseWords("hello world ni hao"))