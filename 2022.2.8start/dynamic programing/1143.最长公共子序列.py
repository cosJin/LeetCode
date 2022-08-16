#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        t1 = len(text1)
        t2 = len(text2)
        dp=[[0 for _ in range(t2)] for _ in range(t1)]
        for i in range(t1):
            if text2[0]==text1[i]: dp[i][0]=1
            else:dp[i][0] = dp[i-1][0]
        for i in range(t2):
            if text1[0]==text2[i]: dp[0][i]=1
            else:dp[0][i]=dp[0][i-1]


        for i in range(t1)[1:]:
            for j in range(t2)[1:]:
                if text1[i] == text2[j]:
                    dp[i][j]= dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
# @lc code=end
print(Solution().longestCommonSubsequence("bsbininm","jmjkbkjkv"))

#    j  m  j  k  b  k  j  k  v
# b [0, 0, 0, 0, 1, 1, 1, 1, 1],
# s [0, 0, 0, 0, 1, 1, 1, 1, 1],
# b [0, 0, 0, 0, 2, 2, 2, 2, 2],
# i [0, 0, 0, 0, 2, 2, 2, 2, 2],
# n [0, 0, 0, 0, 2, 2, 2, 2, 2],
# i [0, 0, 0, 0, 2, 2, 2, 2, 2],
# n [0, 0, 0, 0, 2, 2, 2, 2, 2],
# m [0, 1, 1, 1, 2, 2, 2, 2, 2]]