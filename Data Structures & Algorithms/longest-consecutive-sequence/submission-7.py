class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        s = set(nums)
        best = 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                next_num = num + 1
                while next_num  in s:
                    length += 1
                    next_num += 1
                best = max(length, best)
        return best