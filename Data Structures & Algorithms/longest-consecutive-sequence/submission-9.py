class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = []
        longest = 0

        for num in nums:
            l, r = num - 1, num + 1
            counter = 1
            while num not in seen and l in nums or r in nums:
                if l in nums:
                    seen.append(l)
                    l -= 1
                    counter += 1
                elif r in nums:
                    seen.append(r)
                    r += 1
                    counter += 1 
            longest = max(counter, longest)
        
        return longest
                    

