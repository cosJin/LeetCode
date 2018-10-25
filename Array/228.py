class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:return []
        elif(len(nums)==1):return [str(nums[0])]
        result=[]
        begin=nums[0]
        last=nums[0]
        for element in nums[1:]:
            if element!=last+1:
                if begin == last:result.append(str(begin))
                elif begin != last :result.append(str(begin)+"->"+str(last))
                if element==nums[-1]:
                    result.append(str(element))
                begin = element
                last = element
            elif element == last+1:
                if element==nums[-1]:
                    result.append(str(begin)+"->"+str(element))
                last = element
        return result


class Solution2:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:return []
        elif(len(nums)==1):return [str(nums[0])]
        result=[]
        nums=nums+[nums[-1]]     #若不增加一个元素，最后一段数字总是不显示的，所以最后增加一个元素作为最后一段。
        begin=nums[0]
        last=nums[0]
        for element in nums[1:]:
            if element!=last+1:
                if begin == last:result.append(str(begin))
                elif begin != last :result.append(str(begin)+"->"+str(last))
                begin = element
                last = element
            elif element == last+1:
                last = element
        return result




test = Solution()
print(test.summaryRanges([0,1,2,4,5,7]))
                        