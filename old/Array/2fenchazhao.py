array = []
left, right = 0, len(array)-1
while left <= rihgt:
    mid = (left+right)/2
    if array[mid] == target: return
    elif array[mid] < target:
        left = mid+1
    else:
        right = mid-1
