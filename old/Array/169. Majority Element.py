class Solution:
    def majorityElement(self, nums):
        #暴力法、
        # 字典法 遍历一遍记住个数，O(n)
        #sort法   O(nlogn)
        #分治的方法：左右分别调用本函数 O(nlogn)  只针对这个题目，
        # 如果不是最大的多于一半多，则可能不适用
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return(nums[int(len(nums)/2)])
test=Solution()
print(test.majorityElement([2,1,2,3,4,3,2,2,2]))
