class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #暴力迭代：几层循环，记录个数
        #动态规划：
        # 状态定义：类似于上楼梯问题 dp[i]上到第i个台阶最少步数
        # 状态转移方程：dp[i] = min[dp[i-coins[j]]] + 1   coins 表示所有面值
        # 结果存在最后一个里面   O(mn)
        for i in range(amount):
            for j in coins:
                dp[i] = min(dp[i],dp[i - coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]