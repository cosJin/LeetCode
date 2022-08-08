#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # next = [0]
        # while next:
        #     print(next)
        #     tmp=[]
        #     for n in next:
        #         print(n)
        #         if n >= len(nums)-1:return True
        #         for j in range(nums[n]+1)[1:]:
        #             print(j)
        #             tmp.append(n+j)
        #     next = tmp[:]
        # return False
        if nums[0] == 0 and len(nums)>1:return False
        if len(nums) == 1:return True
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums))[1:]:  #往后遍历
            
            if nums[i-1]>0 and dp[i-1]==1:dp[i]=1  #如果上一个值大于0且能到上个地方，则当前也能到 
            else:
                tmp = []
                for j in range(i+1)[1:]:   #上个是零或者到不了的情况，再往前面的前面取遍历
                    if nums[i-j]>=j and dp[i-j]==1:
                        tmp.append(j)
                        dp[i] = 1
                        break
                if tmp==[]:return False
        return dp[-1]==1
class Solution1(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)   #思想是标记最后一个，然后往前遍历，能到倒数第二个就行...到倒数第三个就行...到第零个就行.
        right_most = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= right_most:
                right_most = i
        return right_most == 0   # or dp[0]
# @lc code=end

print(Solution().canJump([1,0,1,0]))
