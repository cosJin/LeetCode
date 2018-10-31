class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        len = 0
        maxlen = 0
        top = 0
        dic = {}
        for char in s:
            while(char in dic):
                dic.pop(s[top])
                top += 1
                len -= 1
            dic[char] = 1
            len += 1
            maxlen = max(maxlen,len)
        return maxlen
text = Solution()
print(text.lengthOfLongestSubstring("bbbbbbb"))
            

