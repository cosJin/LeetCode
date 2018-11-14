class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for d in range(k+1)[1:]:
            for i in range(len(nums)-d):
                if nums[i] == nums[i+d]:
                    return True
        return False
test = Solution()
print(test.containsNearbyDuplicate([3,3],2))