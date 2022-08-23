#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子数组
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_min = [0 for _ in range(len(nums))]
        dp_max = [0 for _ in range(len(nums))]
        dp_min[0] = dp_max[0] = nums[0]
        for i in range(len(nums))[1:]:
            dp_min[i] = min(nums[i]*dp_min[i-1],nums[i],nums[i]*dp_max[i-1])
            dp_max[i] = max(nums[i]*dp_max[i-1],nums[i],nums[i]*dp_min[i-1])
        return max(dp_max)


# @lc code=end

print(Solution().maxProduct([2,3,-2,4]))