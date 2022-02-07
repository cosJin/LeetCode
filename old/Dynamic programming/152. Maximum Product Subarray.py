class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #暴力求解，用迭代。
        #DP：两步：1、状态的定义；DP[i][0]表示从0开始到包含i的子序列乘积的最大值,
        # DP[i][1]表示从0开始到包含i的子序列乘积的负的最大值,
        # 所以最后要求的就是DP[n-1]，DP[n-2]...DP[0]中最大的
        # 2、DP方程：DP[i+1] = DP[i] * a[i+1] 要判断a[i+1]的正和负
        #dp[i,0] = if a[i]>0: dp[i-1,0] * a[i]
        #dp[i,0] = if a[i]<0: dp[i-1,1] * a[i]
        #dp[i,1] = if a[i]>0: dp[i-1,1] * a[i]
        #dp[i,1] = if a[i]<0: dp[i-1,0] * a[i]
        if nums is None: return 0
        dp = [[0 for _ in range[2]] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]
        for i in range(1,len(nums)):
            x, y = i % 2,(i-1) % 2  #因为存储数组只有两行，所以用这种方式反复利用这两行
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max[res,dp[x][0]]
        return res