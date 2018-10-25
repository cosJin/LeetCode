class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return(nums[int(len(nums)/2)])
test=Solution()
print(test.majorityElement([2,1,2,3,4,3,2,2,2]))
