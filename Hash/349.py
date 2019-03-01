class Solution:
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
        return res
class Solution2:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1 & n2)
test = Solution2()
print(test.intersection([1,2,2,1],[2,2]))