class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #方法一：bfs 对一个单词的每个字母进行增删改 三个分路。
        #方法二：dp
        # dp状态定义：dp[i][j] 第一字符串的前i个字符，j表示单词二的前j个字符。
        # 状态转移方程：如果w1[i] == w2[j]:  dp[i][j] = dp[i-1][j-1]
        #              如果 ！= ：增 删 改。dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])