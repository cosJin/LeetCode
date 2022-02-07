class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeronum = 0
        for element in nums:
            print(element)
            if element == 0:
                zeronum+=1
                nums.append(0)
        for i in range(zeronum):
            nums.remove(0)
        return nums
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        position = 0
        for element in nums:
            if element != 0:
                nums[position]=element
                position+=1
        while position<len(nums):
            nums[position]=0
            position+=1
        return nums
test=Solution()
print(test.moveZeroes2([0,0,0,0,1,2]))
        