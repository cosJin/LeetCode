class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:return[]
        nums.sort()
        print(nums)
        res = set()
        for i,n in enumerate(nums):
            if i>=1 and n==nums[i-1]:continue
            dir = set()
            for j in range(len(nums))[i+1:]:
                if nums[j] not in dir:
                    dir.add(-(nums[j]+nums[i]))
                else:
                    res.add( (nums[i],nums[j],-(nums[j]+nums[i])) )
        return list(map(list,res))


        #时间太久
        # nums.sort()
        # tmp = []
        # res = []
        # for i in range(len(nums)):
        #     target = -nums[i]
        #     j = i+1
        #     k = len(nums)-1
        #     while j < k:
        #         if nums[j] + nums[k] < target:
        #             j += 1
        #         elif nums[j] + nums[k] > target:
        #             k -= 1
        #         else:
        #             tmp.append([nums[i],nums[j],nums[k]])
        #             j+=1
        #             k-=1
        # for i in tmp:
        #     if i not in res:
        #         res.append(i)
        # return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))
            
        


#重复的太多了
    #     if len(nums)<3:return []
    #     elif len(nums) == 3 and sum(nums) != 0:return []
    #     else:
    #         res = []
    #         for i,n in enumerate(nums):
    #             tmp=self.twoSum(nums[:i]+nums[i+1:],-n)
    #             print(tmp)
    #             if len(tmp) > 0:
    #                 tmp = [t+[n] for t in tmp]
    #                 res += tmp
                
    #         return res

    # def twoSum(self,nums,target):
    #     res = []
    #     for i in range(len(nums)):
    #         for j in range(len(nums))[i+1:]:
    #             if nums[i] + nums[j] == target:
    #                 res.append([nums[i],nums[j]])
    #     return res


#还是会有重复的
            # res = []
        # for i in range(len(nums)):
        #     for j in range(len(nums))[i+1:]:
        #         for k in range(len(nums))[j+1:]:
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.append([nums[i],nums[j],nums[k]])
        # return res
