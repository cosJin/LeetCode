class Solution:
    def climbStairs(self, n: int) -> int:
        #方法一：递归，每一步都搜索两种情况
        #递归法从终点开始看，fn = fn-1 + fn-2

        #方法二：动态规划:
        #动态规划从下面开始走，每上一个台阶就记录下步数  O(n)   
        # 甚至不需要记录所有的步数，只需要记录前两个数即可,省内存。
        if n<=2: return n
        mem[0] = 1
        mem[1] = 2
        for i in range(n)[2:]:
            men[i] = men[i-1] + men[i-2]  #不用存所有的，可以继续优化
        return mem[n-1]


        one_before = 2
        two_before = 1
        int all_ways = 0
        for i in range(n)[2:]:
            all_ways = one_before + two_before
            two_before = one_before
            one_before = all_ways
            one_before, two_before = one_before + two_before, one_before
        return all_ways