class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, -val)

        idle = deque()
        cycle = 0
        while heap or idle:
            cycle += 1
            if not heap:
                cycle = idle[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    idle.append([cnt, cycle + n])
            
            if idle and idle[0][1] == cycle:
                heapq.heappush(heap, idle.popleft()[0])
        
        return cycle