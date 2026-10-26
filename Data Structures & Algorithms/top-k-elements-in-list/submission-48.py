class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        vals = set(nums)
        freq = Counter(nums)
        for num in vals:
            heapq.heappush(heap, (-freq[num], num))

        retVal = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            retVal.append(val)
        return retVal
