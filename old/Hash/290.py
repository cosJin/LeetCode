class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        strList = str.split()
        dic = {}
        if len(pattern) != len(strList):return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in dic.keys(): dic[pattern[i]] = strList[i]
                elif dic[pattern[i]] != strList[i]:return False
            return True if len(set(dic.keys()))==len(set(dic.values())) else False
test = Solution()
print(test.wordPattern('aaba','dog cat cat dog'))




