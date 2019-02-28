class Solution:
    def isIsomorphic(self, s: str, t: str):
        dic1  = {}
        dic2  = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dic1.keys():
                    dic1[s[i]] = t[i]
                elif dic1[s[i]] != t[i]:
                    return False
                if t[i] not in dic2.keys():
                    dic2[t[i]] = s[i]
                elif dic2[t[i]] != s[i]:
                    return False
            return True



test = Solution()
print(test.isIsomorphic('add','egg'))