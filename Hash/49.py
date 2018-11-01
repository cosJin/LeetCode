class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == []: return []
        dic = {}
        for word in strs:
            wordList = list(word)
            wordList.sort()
            key = "".join(wordList)
            if key in dic:
                dic[key].append(word)

            else:
                dic[key] = [word]
        return list(dic.values())

test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
