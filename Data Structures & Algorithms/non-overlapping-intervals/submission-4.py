class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        count = 0
        curr_end = -50001
        for interval in intervals:
            start, end = interval
            if curr_end > start:
                count += 1
                continue
            else:
                curr_end = end
            
        return count