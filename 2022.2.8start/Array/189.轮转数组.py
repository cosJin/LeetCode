#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 轮转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)   #要考虑当k大于len(nums)的情况
        nums[:] = nums[-k:]+nums[:-k]  #直接nums = ... 是将nums的指针指向新地址
                                        #nums[:] = ... 是修改nums中的每个值 
        return nums
# @lc code=end
print(Solution().rotate([1,2,3,4,5,6,7],3))
