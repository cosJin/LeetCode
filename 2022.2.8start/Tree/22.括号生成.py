#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(now,l,r):
            if l == 0 and r == 0:
                res.append(now)
            elif l== 0:
                helper(now+')',l,r-1)
            elif l == r:
                helper(now+'(',l-1,r)
            elif l<r:
                helper(now+'(',l-1,r)
                helper(now+')',l,r-1)
        helper('',n,n)
        return res


# @lc code=end

print(Solution().generateParenthesis(3))

