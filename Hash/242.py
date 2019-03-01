class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        else:
            dic1 = {}
            dic2 = {}
            for a in s:
                if a in dic1.keys(): dic1[a]+=1
                else:dic1[a] = 1
            for b in t:
                if b in dic2.keys(): dic2[b]+=1
                else:dic2[b] = 1
        return True if dic1 == dic2 else False
test = Solution()
print(test.isAnagram('anagram','nagaram'))

