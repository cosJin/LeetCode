#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        par = {')':'(',']':'[','}':'{'}
        for i in s:
            if i in par:
                if stack !=[] and stack[-1] == par[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0

            

            
# @lc code=end

