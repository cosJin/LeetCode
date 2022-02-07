class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows >= len(s): return s
        row = -1
        to = 1      #标记方向，0表示向下，1表示向上。
        i=0       
        result=['']*numRows
        while(i<len(s)):
            row += to
            result[row]+=s[i]
            if row == numRows-1:
                to = -1
            elif row == 0:
                to = 1
            i+=1
        return ''.join(result)

test = Solution()
print(test.convert('PAYPALISHIRING',1))