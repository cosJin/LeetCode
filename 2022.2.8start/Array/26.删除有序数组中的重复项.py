#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: return 0
        a,b = 0,0
        while b < len(nums):
            if nums[a] == nums[b]:
                b += 1
            else:
                a += 1
                nums[a],nums[b] = nums[b],nums[a]
                b+=1
        return a+1


# @lc code=end

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2: return 1
        
        s,f = 0, 1
        
        while f < len(nums):
            if nums[s] == nums[f]:
                f += 1
            else:
                s += 1
                nums[s] = nums[f]
                f += 1
                
        return s + 1
            