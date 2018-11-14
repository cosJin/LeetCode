class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dic = dict(zip(list(range(n-3)+2),[1]*(n-2)))
        # dic = dict(zip(list(range(n)[2:]),[1]*(n-2)))
        # for i in range(n)[2:]:
        #     for key in dic.keys():
        #         if key%i == 0 and key/i!=1:
        #             dic[key] = 0
        # return list(dic.values()).count(1)
        l = list(range(n))[2:]
        for i in range(n)[2:]:
            for element in l:
                if element%i == 0 and element/i!=1:
                    l.remove(element)
        return len(l)
test = Solution()
print(test.countPrimes(10000))
