#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
from email import header


class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type heights: List[int]
        :rtype: int
        """
    #遍历法，超时了
        # area = 0
        # for l in range(len(heights)+1)[1:]:
        #     for i in range(len(heights)-l+1):
        #         area = max(area,l*min(heights[i:i+l]))
        # return area
    #思路不对
        # h = []
        # area=0
        # for n,i in enumerate(heights):
        #     if i!=0:
        #         h.append(i)
        #     if n==len(heights)-1 or i==0:
        #         while len(h)>=1:
        #             if len(h) != 1:
        #                 area = max(area,len(h)*min(h))
        #             else:
        #                 area = max(area,h[0])
        #             if h[0]>=h[-1]:
        #                 h = h[0:-1]
        #             else:
        #                 h = h[1:]
        #         h=[]
        # return area
    #关键思想是：某个矩形条能构成的最大面积取决于它左右两侧第一个比他小的元素位置。
#抄的   栈的思想，新入栈的元素，左侧第一个比他小的值为它栈下侧的元素，新进来的元素若比当前栈顶元素小，则新进来的元素为栈顶右侧第一个比他小的元素。
#抄的---------
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans
                
# @lc code=end
print(Solution().largestRectangleArea([2,1,0,4,5,6]))

