class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        for idx in range(len(nums)):
            find = target - nums[idx]
            print(vals, find)
            if find in vals:
                return [vals[find], idx] 
            else:
                vals[nums[idx]] = idx
        return
        