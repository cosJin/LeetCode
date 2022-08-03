#
# @lc app=leetcode.cn id=126 lang=python
#
# [126] 单词接龙 II
#

# @lc code=start
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # def diff(a,b):
        #     res = 0
        #     for i in range(len(a)):
        #         if a[i]!= b[i]:res+=1
        #     return res

        # wordList = list(set(wordList))
        # if endWord not in wordList:return []


        # now = [[beginWord,[beginWord]]]
        # next = []
        # res = []
        # while  now != []:
        #     for (now_word,path) in now:
        #         if now_word == endWord:res.append(path)
        #         to_del = set()
        #         for word in wordList:
        #             if diff(word,now_word) == 1:
        #                 t = path[:]
        #                 t.append(word)
        #                 next.append([word,t])
        #                 to_del.add(word)
        #     for i in to_del:
        #         wordList.remove(i)
        #     now = next
        #     next = []
        # return res
        lt = 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        now = [[beginWord,[beginWord]]]
        next = []
        res = []
        while  now != [] and res ==[]:
            for (now_word,path) in now:
                if now_word == endWord:res.append(path)
                to_del = set()
                for l in lt:
                    for j in range(len(now_word)):
                        if now_word[:j]+l+now_word[j+1:] in wordList: 
                            t = path[:]
                            t.append(now_word[:j]+l+now_word[j+1:])
                            next.append([now_word[:j]+l+now_word[j+1:],t])
                            to_del.add(now_word[:j]+l+now_word[j+1:])
            for i in to_del:
                wordList.remove(i)
            now = next
            next = []
        return res
# @lc code=end

print(Solution().findLadders('hit','cog',["hot","dot","dog","lot","log","cog"]))
