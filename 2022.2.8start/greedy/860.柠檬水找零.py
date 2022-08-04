#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        #因为只能有5 10 20元，所以穷举一下就行
        change = {5:0, 10:0}

        for bill in bills:
            if bill == 5:
                change[5] += 1 

            elif bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
                    
            else:
                if change[10]>0 and change[5]>0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >=3:
                    change[5] -= 3
                else:
                    return False
        return True
# @lc code=end

