
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1: return [[1]]
        elif numRows==2: return [[1],[1,1]]
        elif numRows==0: return []
        else:
            result=[]
            result.append([1])
            result.append([1,1])
            while(numRows-2>0):
                a=[]
                for index in range(len(result[-1])-1):
                    a.append(result[-1][index]+result[-1][index+1])
                a=[1]+a+[1]
                result.append(a)
                numRows-=1
        return result
test=Solution()
print(test.generate(3))

