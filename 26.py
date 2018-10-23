class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:return(0)
        lastOne=None
        position=0
        for i in range(len(nums)):
            if nums[i]!=lastOne:
                nums[position]=nums[i]
                lastOne=nums[i]
                position+=1
        return(position)
            