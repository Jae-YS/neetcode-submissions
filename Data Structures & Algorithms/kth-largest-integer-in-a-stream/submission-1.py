class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        for i in range(len(nums)):
            self.nums[i] *= -1
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        temp = self.nums.copy()

        val = 0
        for _ in range(self.k):
            val = -heapq.heappop(temp)
        return val
