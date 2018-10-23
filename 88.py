class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=m-1
        j=n-1        
        position=len(nums1)-1
        while(i>=0 and j>=0):
            if(nums1[i]>=nums2[j]):
                nums1[position]=nums1[i]
                i-=1
                position-=1
            elif(nums1[i]<nums2[j]):
                nums1[position]=nums2[j]
                j-=1
                position-=1
        if j==-1:pass
        elif i==-1:
            nums1[0:position+1]=nums2[0:j+1]
        
        
test=Solution()
print(test.merge([1,2,3,0,0,0],3,[2,5,6],3))