class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:return ""
        elif len(strs)==1:return strs[0]
        prefix = ""
        for i in range(len(strs[0])):
            prefix = strs[0][0:i+1]
            for str in strs:
                if str[0:i+1] == prefix:
                    continue
                else:
                    i -= 1
                    if i==-1:
                        return ""
                    else: return strs[0][0:i+1]
test = Solution()
print(test.longestCommonPrefix(["f3","f3","f3"]))