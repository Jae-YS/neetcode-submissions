import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_heap = []
        for idx, val in enumerate(profits):
            heapq.heappush(max_heap, (-val, idx))

        profit = w
        selected_projects = 0
        while selected_projects < k:
            passed_projects = []
            
            while max_heap:
                val, idx = heapq.heappop(max_heap)
                if capital[idx] <= profit:
                    print(-val, idx) 
                    val = -val
                    profit += val
                    selected_projects += 1                   
                    break
                else:
                    heapq.heappush(passed_projects, (val, idx))

            if len(passed_projects) == len(profits):
                return profit
            
            for projects in passed_projects:
                heapq.heappush(max_heap, projects)
            

        return profit