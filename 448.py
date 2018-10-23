# class Solution:
#     def findDisappearedNumbers(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result = []
#         tag=nums
#         for ele in nums:
#             tag[ele-1]=0
#         for i in range(len(tag)):
#             if tag[i]==1: result.append(i+1)
#         return result
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for ele in nums:
            index = abs(ele)-1
            nums[index] = (-nums[index]) if nums[index]>0 else nums[index]
        for l in range(len(nums)):
            if nums[l]>0:
                result.append(l+1)
        return result
test=Solution()
print(test.findDisappearedNumbers([2,3,4,5,5]))
    