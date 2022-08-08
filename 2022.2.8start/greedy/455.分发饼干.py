#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res =0
        g = sorted(g)
        s = sorted(s)
        for n in g:
            tmp = []
            for c in s:
                if c>=n:
                    res+=1
                    s.remove(c)
                    break
                
        return res
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        numOfCookies = 0
        while s and g:
            if s[-1] >= g[-1]:  #思路：拿最大的去喂最大胃口的人！能喂则结果加一，不能喂则胃口最大的人pop掉
                s.pop()
                numOfCookies+=1
            g.pop()
        return numOfCookies
    
# @lc code=end
print(Solution().findContentChildren([1,2,3],[1,1]))

