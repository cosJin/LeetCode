#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    #从前往后一维递推，如果加上当前值后比原来的值大，那么最大序列就加上当前值，如果还不如当前值大，则从当前值开始往后加即可。
        #理解为以i个数字结尾的子序列的和
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(len(nums))[1:]:
            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)
# @lc code=end

