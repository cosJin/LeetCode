class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #状态公式：Max_profit[i]表示第i天的最大收益，
        #递推公式：  考虑：mp[i] = mp[i-1] + - a[i]   表示买入股票
        #                mp[i] = mp[i-1] +  a[i]   表示卖出股票
        #上面缺少股票数量信息

        #需要增加一维mp[i][j]  i 表示天    j可以0和1，表示有没有股票
        #mp[i][0] = 第i天最大值就是: mp[i-1][0]     前一天没有，今天也没有，表示不动
        #                           mp[i-1][1] + a[i]  前一天有一股，今天卖了
        #mp[i][1] = mp[i-1][1]  今天有一股的话就是 昨天有一股今天不动
        #或者     = mp[i-1][0] - a[i]  或者 昨天没有，今天买了
        #
        # 以上仍缺少买卖次数的信息，还需要添加一个维度
        #mp[i][j][k]   其中k表示之前交易了多少次。
        #mp[i,k,0] = 前一天没有股票且今天不动    mp[i-1,k,0]
        #     or   = 前一天有股票，今天卖了      mp[i-1,k-1,1] + a[i]二者取最大。

        #mp[i,k,i] = max:   mp[i-1,k, 1]  mp[i-1,k-1,0] -a[i]
        if not prices: return 0
        res = 0
        profit = [[0 for i in rang(3)] for i in range(len(prices))]
        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0
        #0,1,2表示 没买股票，买了没卖股票，卖了股票

        for i in range(1,len(prices)):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1],profit[i-1][0] - price[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            res = max(res,profit[i][0],profit[i][1],profit[i][2])
        return res