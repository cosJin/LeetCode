class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dic = 0
        for i in range(len(nums)):
            if i%2 == 0:
                dic+=nums[i]
            elif i%2 == 1:
                dic-=nums[i]
        return dic

test = Solution()
print(test.singleNumber([1,2,1,4,4,2,3]))