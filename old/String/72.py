class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0]*(len(word2)+1) for i in range(len(word1)+1)]  # word1行word2列
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(len(word1)+1)[1:]:
            for j in range(len(word2)+1)[1:]:
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1,dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[-1][-1]
test = Solution()

a = ['民心','將','移','乃','難','親']
b = ['民心','將','移乃','難','親']
print(test.minDistance(a,b)) #用较多的长度减去错误长度就是对的个数