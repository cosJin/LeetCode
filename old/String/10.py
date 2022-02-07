class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False]*(len(s)+1) for i in range(len(p)+1)]  # p行s列
        dp[0][0] = True
        for i in range(len(p)+1)[1:]:
            dp[i][0] = (i>=2) and (p[i-1] == '*') and (dp[i-2][0]) 
        for i in range(len(p)+1)[1:]:
            for j in range(len(s)+1)[1:]:
                if p[i-1] == '*':
                    dp[i][j] = (dp[i][j-1]==True and (s[j-1]==p[i-2] or p[i-2] == '.')) or (dp[i-1][j] == True) or (dp[i-2][j] == True)
                elif p[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] == True and p[i-1] == s[j-1]
        return dp[len(p)][len(s)]
a = Solution()
print(a.isMatch("aba","aba*"))
        
