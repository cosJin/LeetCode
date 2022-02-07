class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # vowel = ["a","e","i","o","u","A","E","I","O","U"]   
        vowel = set("aeiouAEIOU")           #似乎用set比较快,不知道为什么。
        b = 0
        e = len(s)-1
        s = list(s)
        while(b<e):
            if s[b] in vowel and s[e] in vowel:
                s[e],s[b] = s[b],s[e]
                b += 1
                e -= 1
            # elif s[e] not in vowel:      #这三个if可以简化为两个if。
            #     e -= 1
            # elif s[b] not in vowel:
            #     b += 1
            # else:
            #     e -= 1
            #     b += 1
            if s[e] not in vowel:
                e -= 1
            if s[b] not in vowel:
                b += 1
        return "".join(s)

test = Solution()
print(test.reverseVowels("leetcode"))
        
        