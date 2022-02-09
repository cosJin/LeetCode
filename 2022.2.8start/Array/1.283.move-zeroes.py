class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return nums
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))
#快慢指针，快指针如不为零，就和慢指针交换，且慢指针+1