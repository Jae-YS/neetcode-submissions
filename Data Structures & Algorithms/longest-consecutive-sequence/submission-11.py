class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            l, r = num - 1, num + 1
            counter = 1
            while l in nums or r in nums:
                if l in nums:
                    l -= 1
                    counter += 1
                elif r in nums:

                    r += 1
                    counter += 1 
            longest = max(counter, longest)
        
        return longest
                    

