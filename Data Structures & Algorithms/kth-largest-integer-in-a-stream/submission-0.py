class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        for i in range(len(nums)):
            nums[i] *= -1
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        temp = self.heap[:]
        val = -1
        for _ in range(self.k):
            val = -heapq.heappop(temp)
        
        return val

