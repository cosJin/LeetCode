#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 省份数量
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        res = 0
        for person in isConnected:
            stack=[]
            for n,i in enumerate(person):   #遍历每一个用户的关系,加到stack中,再遍历每个关系人物的关系,   注意将遍历过的点做标记.
                if i == 1:
                    stack.append(n)
                    person[n]=0
            while stack != []:
                p=stack.pop()              #BFS方法,  看别人答案可以dfs
                for nn,ii in enumerate(isConnected[p]):
                    if ii==1:
                        stack.append(nn)
                        isConnected[p][nn]=0
                if stack == []:            # 直到一个人的所有关系都遍历完后,res+=1
                    res+=1
        return res
                    

# @lc code=end

print(Solution().findCircleNum( [[1,1,0],[1,1,0],[0,0,1]]))
