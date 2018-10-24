class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:return ""
        elif "" in strs: return ""
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
            if i == len(strs[0])-1:return strs[0]
class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        if not strs: return ''
				#since list of string will be sorted and retrieved min max by alphebetic order
        s1 = min(strs)
        s2 = max(strs)

        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i] #stop until hit the split index
        return s1
test = Solution2()
print(test.longestCommonPrefix(["fine","fimed","fifm"]))