class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        count = 0
        cs, ce = intervals[0]
        for i in range(1, len(intervals)):
            nc, ne = intervals[i]
            if ce <= nc:
                cs, ce = nc, ne
            else:
                count += 1
                ce = min(ce, ne) 

        return count