class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        position=0
        for i in nums:
            if(i!=val):
                nums[position]=i
                position+=1
        return position