"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        max_room = 0
        i = j = 0
        count = 0
        while i < len(starts) and j < len(ends):
            cur_start, cur_end = starts[i], ends[j]
            if cur_start < cur_end:
                count += 1
                max_room = max(max_room, count)
                i += 1
            else:
                count -= 1
                j += 1

        return max_room