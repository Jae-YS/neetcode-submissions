"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        
        max_room = 0
        count = 0
        for i in sorted(mp.keys()):
            count += mp[i]
            max_room = max(count, max_room)
        return max_room