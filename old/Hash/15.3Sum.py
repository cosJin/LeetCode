class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #法一：暴力，三层循环O(n^3)
        #法二，遍历前两个数组，从最后一个数组中寻找-(a+b)   从set中寻找数只需要O(1)，
        #所以总复杂度为O(n^2)，但需要另外的n的空间
        #方法三：sort and find，先整个数组进行排序nlogn    
        #第一层循环不能少，枚举a，从a后面找b和c，用两边往中间找的方法，如果a+b+c大于目标，
        #则c往左移动一位，如果三数之和小于目标，则b右移一位。O(n^2)复杂度，
        # 但是不用重新开辟一个空间。
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v,-v-x,x))
        return map(list,res)
    def threeSumself1(self,nums):#自己默写的方法一
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i,x in enumerate(nums[:-2]):
            if i >= 1 and x == nums[i-1]:
                continue
            tmp = {}
            for y in nums[i+1:]:
                if y in tmp: 
                    res.add((x,y,-x-y))
                else:
                    tmp[-x-y] = 1
        return res

    def threeSumself2(self,nums):#自己默写的方法二
    def threeSum2(self, nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1,len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:l += 1
                elif s > 0:r -= 1
                else:
                    res.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1;r-=1
a = Solution()
answer = a.threeSumself([-1,1,0,-2,2,3,4,5,-6])
print(list(answer))