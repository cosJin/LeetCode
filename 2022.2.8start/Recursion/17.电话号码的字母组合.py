#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dir = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        if len(digits) == 0:return []
        def helper(dig,input):
            if len(dig) == 0:
                return input
            res = []
            ls = dir[dig[0]]
            for r in input:
                for l in ls:
                    res.append(r+l)
            return helper(dig[1:],res)
        return helper(digits,[''])

# @lc code=end

print(Solution().letterCombinations('23'))