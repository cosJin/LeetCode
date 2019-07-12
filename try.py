nums=[2,1,5,4,3,6,3,7,5]
k = 3
window, res = [],[]
for i, x in enumerate(nums):
    if i>= k and window[0] <= i-k:  #进来元素，窗口内元素个数控制在k个
        window.pop(0)
    while window and nums[window[-1]] <= x:     #从window右边开始依次比较，比x小的均弹出，
                                                #保证window中左边的数都比右边的大
        window.pop()
    window.append(i) #上面将pop的情况都考虑完后，放心大胆的append即可。
    if i>= k-1:  #保证窗口中不足k个数（开头的时候）的时候不会输出。
        res.append(nums[window[0]])