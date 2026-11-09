class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in save:
                return [save[diff], i]
            
            save[num] = i
            