class Solution(object):
    def twoSum(self, nums, target):
        res = {}
        for n,v in enumerate(nums):
            if target-v not in res:
                res[v] = n
            else:
                return [res[target-v],n]
print(Solution().twoSum([2,7,44,34],9))