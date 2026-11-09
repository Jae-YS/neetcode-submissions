from collections import deque
import heapq

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        l = 0
        count = 0
        
        for s, e in meetings:
            if s > l + 1:
                count += s - l - 1
            l = max(l, e)
        
        count += max(0, days - l)
        return count