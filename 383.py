class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # r = list(ransomNote)
        # m = list(magazine)
        r = ransomNote
        m = magazine
        for i in r:
            if i in m:
                # m.remove(i)
                m = m.replace(i,'',1)  #相当于从字符串中删除i
            else:return False
        return True
test = Solution()
print(test.canConstruct('a','aba'))