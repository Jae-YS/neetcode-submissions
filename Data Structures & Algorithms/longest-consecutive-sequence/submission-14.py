class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)
        cur = {}
            
        cur_max = 0
        for num in val:
            if num - 1 not in val:
                count = 0
                while num in val:
                    count += 1
                    num += 1
                cur_max = max(cur_max, count)
            
        
        return cur_max