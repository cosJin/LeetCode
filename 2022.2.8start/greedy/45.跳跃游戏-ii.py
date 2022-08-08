#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:return 0
        dp = [0] * len(nums)
        for i in range(len(nums))[::-1]:
            # print(i,dp)
            if i+nums[i]>=len(nums)-1:dp[i]=1
            elif nums[i]==0:dp[i]=float('inf')
            else:
                tmp =[]
                for j in range(nums[i]+1)[1:]:
                    # print('j:',j)
                    tmp.append(dp[i+j])
                dp[i] = min(tmp)+1
        return dp[0]
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        cur = 0
        farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i]) #最远能到的位置
            if i == cur:
                result += 1
                cur = farthest
        return result
# @lc code=end

print(Solution().jump([2,3,0,1,4]))