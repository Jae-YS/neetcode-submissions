class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            
            diff = s1 - s2
            if diff:
                heapq.heappush(heap, -diff)

        return -heap[0] if heap else 0
