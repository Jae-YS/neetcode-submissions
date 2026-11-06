class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ma = {}
        for x, y, t in times:
            ma.setdefault(x, []).append((t, y))
        visited = set()
        min_time = [float('inf')] * n
        min_time[k - 1] = 0
        visit = ma.get(k, [])
        heapq.heapify(visit)
        while visit:
            cost, nex = heapq.heappop(visit)
            min_time[nex - 1] = min(min_time[nex - 1], cost)
            for c, ne in ma.get(nex, []):
                if (nex, ne) not in visited:
                    visited.add((nex,ne))
                    heapq.heappush(visit, (c + cost, ne))            

        if float('inf') in min_time:
            return -1
        return max(min_time)