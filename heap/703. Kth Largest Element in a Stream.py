#方法一：排序，取前k大的元素，后面加元素，如果比k个数中最小元素大，
#则加入k，对新的k个进行排序。
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.kl = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.kl) < self.k:
            self.kl.append(val)
            self.kl.sort(reverse=True)
        elif val > self.kl[-1]:
            self.kl.pop()
            self.kl.append(val)
            self.kl.sort(reverse=True)
        return self.kl[-1]
#使用python内置的heapq 小顶堆， 维护大小为k的小顶堆。
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool, self.k = nums, k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)