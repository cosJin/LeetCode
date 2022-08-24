#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:return nums[0]
        elif len(nums) == 2:return max(nums)
        elif len(nums) == 3:return max(nums[1],nums[0]+nums[2])
        else:
            dp = [0 for _ in range(len(nums))]
            dp[0]=nums[0]
            dp[1]=nums[1]
            dp[2]=nums[2]+nums[0]
            for i in range(len(nums))[3:]:
                dp[i] = max(nums[i]+dp[i-2],nums[i]+dp[i-3])
        return max(dp[-1],dp[-2])

# @lc code=end
print(Solution().rob([1,2,3,1]))
