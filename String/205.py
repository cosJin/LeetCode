class Solution:
    def isIsomorphic(self, s: str, t: str):
        dic1  = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] not in dic1.keys():
                    dic1[s[i]] = t[i]
                elif dic1[s[i]] != t[i]:
                    return False
            return False if len(dic1.values()) != len(set(dic1.values())) else True



test = Solution()
print(test.isIsomorphic('add','egg'))