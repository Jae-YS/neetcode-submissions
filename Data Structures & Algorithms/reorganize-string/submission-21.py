from collections import defaultdict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency = defaultdict(int)
        for char in s:
            frequency[char] += 1
        max_frequency = max(frequency.values())
        
        if max_frequency > (len(s) + 1) // 2:
            return ""
            
        chars = []
        new_str = ""
        for key, val in frequency.items():
            chars.append((-val, key))
        heapq.heapify(chars)

        while chars:
            val, key = heapq.heappop(chars)
            if len(new_str) != 0 and key == new_str[len(new_str) - 1]:
                save = (val, key)
                val, key = heapq.heappop(chars)
                heapq.heappush(chars, save)
            new_str += key
            val += 1
            if val != 0:
                heapq.heappush(chars, (val, key))

        return new_str
        

