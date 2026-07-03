class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 0
        idx = 0
        while idx < len(nums):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                nums.pop(idx)
            else:
                idx += 1
        
        return len(nums)