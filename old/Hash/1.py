class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}   # needed num : index
        for index in range(len(nums)):
            if nums[index] in dic.keys():
                return [dic[nums[index]],index]
            dic[target-nums[index]] = index
            

test = Solution()
print(test.twoSum([2,7,5,9],9))