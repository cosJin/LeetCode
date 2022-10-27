#
# @lc app=leetcode.cn id=433 lang=python
#
# [433] 最小基因变化
#

# @lc code=start
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        gene = ['A','C','G','T']
        c = [-1]
        def replace_gene(start,end,bk,ch):
            print(start,end,bk,ch)
            b = bk[:]   #备份一个当前层的bk，保证从当前层往后的迭代中不会影响到原bank
            if start == end: c.append(ch)    #结果怎么回传 需要注意
            for i in range(8):
                for g in gene:
                    if start[:i]+g+start[i+1:] in b:
                        b.remove(start[:i]+g+start[i+1:])
                        replace_gene(start[:i]+g+start[i+1:],end,b,ch+1)
        replace_gene(start,end,bank,0)
        print(c)
        return -1 if len(c)==1 else min(c[1:])

#最短路径显然bfs更符合逻辑，找到即可停止。
#bfs使用queue
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = []
        queue.append((start,0))
        bankSet = set(bank)
        
        while queue:
            curr, step = queue.pop(0)
            if curr == end:
                return step
            for i in range(len(curr)):
                for c in "AGCT":
                    mutation = curr[:i] + c + curr[i+1:]
                    if mutation in bankSet:
                        bankSet.remove(mutation)
                        queue.append((mutation,step+1))
                        
        return -1
       #还可以双向bfs
 

# @lc code=end
print(Solution().minMutation("AAAAAAAA","CCCCCCCC",["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"]))

