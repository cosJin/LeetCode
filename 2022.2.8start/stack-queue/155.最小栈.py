#
# @lc app=leetcode.cn id=155 lang=python
#
# [155] 最小栈
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = float('inf')


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.min = val if val <= self.min else self.min
        self.min_stack.append(self.min)



    def pop(self):
        """
        :rtype: None
        """
        t = self.stack.pop()
        self.min_stack.pop()
        if self.min_stack == []:
            self.min = float("inf")
        else:
            self.min = self.min_stack[-1]





    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

