class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 第一种方法，用大顶堆，维护窗口中的三个数，移动窗口时
        # 要删除一个元素，加一个新元素，输入堆顶元素。增加一个元素维护大顶堆是logn复杂度。 
        # 一共是Nlnk

        # 方法二：直接用Queue，双端队列deque，a.入队列，b，维护：进来一个大的就把左边的元素
        # 弹出，保证三个里面最大的就在最左边。  复杂度为 N    
        # 本题因为只找最大值，不需要维护第二大，第三大的，而大顶堆还维护了第二第三大
        # 值，所以本体还是queue简单一些。
        if not nums: return []
        window, res = [],[]
        for i, x in enumerate(nums):
            if i>= k and window[0] <= i-k:  #进来元素，窗口内元素个数控制在k个
                window.pop(0)
            while window and nums[window[-1]] <= x:  #从window右边开始依次比较，比x小的均弹出，
                                                     #保证window中左边的数都比右边的大
                window.pop()
            window.append(i) #上面将pop的情况都考虑完后，放心大胆的append即可。
            if i>= k-1:  #保证窗口中不足k个数（开头的时候）的时候不会输出。
                res.append(nums[window[0]])
        return res
                
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        window, res = [],[]
        for num,i in enumerate(nums):
            if len(window) < k:
                window.append(num)
