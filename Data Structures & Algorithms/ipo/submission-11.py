import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = [(capital[i], profits[i]) for i in range(len(profits))]
        heapq.heapify(min_heap)

        max_heap = []
        profit = w

        for _ in range(k):
            while min_heap and min_heap[0][0] <= profit:
                cap, p = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -p)


            if not max_heap:
                break

            profit += -heapq.heappop(max_heap)
        return profit