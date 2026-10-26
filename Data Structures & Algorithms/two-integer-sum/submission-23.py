class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in vals:
                return [vals[diff], idx]
            else:
                vals[val] = idx
        
        return [0]