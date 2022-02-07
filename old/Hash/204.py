class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        # """
        # dic = dict(zip(list(range(n)[2:]),[1]*(n-2)))
        # for i in range(int(n**0.5)+1)[2:]:
        #     for key in dic.keys():
        #         if key%i == 0 and key/i!=1:
        #             del dic[key]
        # return list(dic.values()).count(1)
        # l = list(range(n))[2:]
        # for i in range(int(n**0.5)+1)[2:]:
        #     for element in l:
        #         if element%i == 0 and element/i!=1:
        #             l.remove(element)
        # return len(l)
        if n<3: return 0 
        l = [True]*n
        l[0] = False
        l[-1] = False
        for i in range(int(n**0.5)+1)[2:]:
            l[i*i-1:-1:i] = [False]*(len(l[i*i-1:-1:i]))
        return l.count(True)
        # return l


test = Solution()
print(test.countPrimes(3))
