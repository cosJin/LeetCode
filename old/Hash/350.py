class Solution:
    def intersection(self, nums1, nums2):
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
                nums2.remove(n)
        return res
test = Solution()
print(test.intersection([1,2,2,1],[2,2]))