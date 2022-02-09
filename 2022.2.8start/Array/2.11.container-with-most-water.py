class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxi = min(height[left],height[right])*(right-left)
        index_left=left
        index_right=right
        while left<right:
            if height[left] <= height[right]:
                while height[left]<=height[index_left] and left<right:
                    left+=1
                s = min(height[left],height[right])*(right-left)
                index_left=left  ##新left只需要高度大于原left就更新index_left，不要即高，且面积大的时候才更新。
                if s > maxi:
                    maxi=s
            elif height[left] > height[right]:
                while height[right]<=height[index_right] and left<right:
                    right-=1
                s = min(height[left],height[right])*(right-left)
                index_right=right
                if s > maxi:
                    maxi=s
        return maxi
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
        




