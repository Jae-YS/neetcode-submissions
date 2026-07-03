import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lowest = max(piles)
        while l <= r:
            speed = (l + r) // 2

            total_hours = sum((p + speed - 1)//speed for p in piles)
            if total_hours > h:
                l = speed + 1
            elif total_hours <= h:
                lowest = min(lowest, speed)
                r = speed - 1
        return lowest


