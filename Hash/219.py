class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        if len(set(nums)) == len(nums):
            return False
        for i in range(len(nums)):
            try :
                dic[nums[i]]
                if i-dic[nums[i]]<=k:
                    return True
                else: dic[nums[i]] = i
            except:dic[nums[i]] = i
        return False
test = Solution()
print(test.containsNearbyDuplicate([1,2,3,1,2,3],2))