#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         if nums==[]:return []
#         if len(nums)==1:return [[],[nums[0]]]
#         res.append(nums)
#         for i in range(len(nums)):
#             # print(i)
#             res.append(nums[:i]+nums[i+1:])
#             # print(nums[:i]+nums[i+1:])
#             res+=self.subsets(nums[:i]+nums[i+1:])
#         t = []
#         for i in res:
#             if i in t:continue
#             else:t.append(i)
#         return t


class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            print(result)
            for j in range(len(result)):
                result.append(result[j][:])  #切记要带[:]，则为浅拷贝，生成新的列表，如不带[:],则为深拷贝，直接指向原元素，下面进行修改的时候会同时修改两处。
                result[j].append(i)
        return result
# [[]]   先放个[]进去，
# [[1], []] 然后遍历nums中元素i
# [[1, 2], [2], [1], []] 每轮循环保留上一轮结果的同时，给上一轮结果各添加一i

            
# @lc code=end

a = Solution()
print(a.subsets([1,2,3]))