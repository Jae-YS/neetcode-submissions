class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, -val)

        idle = deque()
        cycle = 0
        while heap or idle:
            
            if not heap and idle[0][1] > cycle:
                cycle += 1
                continue
            elif idle and idle[0][1] <= cycle:
                if heap and -heap[0] > idle[0][0]:
                    count = -heapq.heappop(heap)
                    count -= 1
                    cycle += 1
                    if count > 0:
                        idle.append((count, cycle + n + 1))
                    continue
                left, time = idle.popleft()
                left -= 1
                if left > 0:
                    idle.append((left, cycle + n + 1))
            else:
                count = -heapq.heappop(heap)
                count -= 1
                if count > 0:
                    idle.append((count, cycle + n + 1))
            
            cycle += 1
        return cycle