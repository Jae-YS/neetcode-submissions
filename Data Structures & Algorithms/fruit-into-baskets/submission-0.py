class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_seen = {}
        max_fruits = 0

        l = 0
        for i, val in enumerate(fruits):
            last_seen[val] = i

            if len(last_seen) > 2:
                oldest = min(last_seen, key=last_seen.get)
                l = last_seen.pop(oldest) + 1
            
            max_fruits = max(max_fruits, i - l + 1)
                
        return max_fruits
            
