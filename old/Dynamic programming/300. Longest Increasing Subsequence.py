class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #暴力迭代
        #到某个节点，带该节点且之前的节点已经选好了。所以是有最优子结构。
        #状态定义：dp[i] 表示从0 到 i 且第i元素要选上的最长子序列的长度
        #最终结果为dp[0]到dp[n-1]的最大值
        #状态转移方程： dp[i] = max(dp[j] + 1)  j:0->i-1  且a[j]<a[i]   
        # 两层循环  第一层i   后面遍历0 -> i  O(n^2)
        for i in range(n):
            for j in range(0,i):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)