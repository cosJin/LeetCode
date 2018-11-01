class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for word in strs:
            key = "".join(sorted(list(word)))
            if key in dic:
                dic[key].append(word)

            else:
                dic[key] = [word]
            a = list(dic.values())
        return a

test = Solution()
print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
