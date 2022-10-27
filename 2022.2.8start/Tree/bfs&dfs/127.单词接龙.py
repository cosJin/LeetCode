#
# @lc app=leetcode.cn id=127 lang=python
#
# [127] 单词接龙
#

# @lc code=start
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
#测试一个特别大的wordList的时候会超时，所以需要讨论wordList多大，是遍历wordlist划算还是遍历beginword划算
#所以开始对字典set去重很重要
#当字典很大的时候，不如遍历26个字母组成新单词，对字典进行seet后，查询更省时间，方法二所示。
        def diff(a,b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d+=1
            return d
        wordList = list(set(wordList))   #对字典去重
        queue = [beginWord]
        k = 0
        if endWord not in wordList:return 0
        while queue!=[]:
            next = []
            k+=1
            for node in queue:
                tmpList = wordList[:]
                for word in tmpList:
                    if diff(node,word) == 1:
                        next.append(word)
                        if word == endWord:return k+1
                        wordList.remove(word)
            queue = next[:]
        return 0
        # import string
        # wordList = set(wordList)   #去重的同时，方便后面进行查询if in     
        # ls = string.ascii_lowercase # 所有lowercase字母
        # queue = [beginWord]
        # k = 0
        # if endWord not in wordList:return 0
        # while queue!=[]:
        #     print(queue,wordList)
        #     next = []
        #     k+=1
        #     for node in queue:
        #         for i in range(len(beginWord)):
        #             for l in ls:
        #                 new_word = node[:i]+l+node[i+1:]
        #                 if new_word in wordList:
        #                     next.append(new_word)
        #                     if new_word == endWord:return k+1
        #                     wordList.remove(new_word)
        #     queue = next[:]
        # return 0
#还可以双向bfs

# @lc code=end
print(Solution().ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"]))

