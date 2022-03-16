#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {}
        for i in range(len(nums)):
            if target-nums[i] not in res:
                res[nums[i]] = i
            elif target-nums[i] in res:
                return [i,res[target-nums[i]]]
# @lc code=end
