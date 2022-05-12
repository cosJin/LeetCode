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
        # def helper(n,now):
        #     if n==0: 
        #         return now
        #     tmp = []
        #     for i in now:
        #         tmp.append(i+"()")
        #         tmp.append("()"+i)
        #         tmp.append("("+i+")")
        #     tmp = list(set(tmp))
        #     return helper(n-1,tmp)

        # if n == 1:return ["()"]
        # else:
        #     return helper(n-1,["()"])
        res = []
        def helper(l,r,now):
            if l == 0:
                res.append(now + r * ")"  )
            elif l == r: 
                helper(l-1,r,now+"(")
            elif l < r:
                helper(l-1,r,now+"(")
                helper(l,r-1,now+")")

        helper(n,n,"")
        return res

# @lc code=end
print(Solution().generateParenthesis(3))
