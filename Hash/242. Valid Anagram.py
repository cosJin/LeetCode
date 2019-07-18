class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        else:
            dic1 = {}
            dic2 = {}
            for a in s:
                if a in dic1.keys(): dic1[a]+=1
                else:dic1[a] = 1
                # 上面两行可以简化成：dic1.get(a,0)+1  
                # get函数用来获取dic中的某个元素，如果没有则返回设置的默认值。

                #还可以自己建26字母的数组，ord()函数取字母的ascii码
            for b in t:
                if b in dic2.keys(): dic2[b]+=1
                else:dic2[b] = 1
        return True if dic1 == dic2 else False
        #方法一：对两个单词进行排序，然后比较两个单词是否相等。复杂度nlogn 
        #方法：return sorted(s) == sorted(t)
        #方法二：用map对单字中的字母进行计数。{letter：count}。复杂度 n
test = Solution()
print(test.isAnagram('anagram','nagaram'))

