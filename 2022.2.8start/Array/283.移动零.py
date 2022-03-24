#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = b = 0
        while b<len(nums):
            if nums[b] == 0: 
                b+=1
            elif nums[b] != 0:
                nums[a],nums[b] = nums[b],nums[a]
                a+=1
                b+=1
# @lc code=end

