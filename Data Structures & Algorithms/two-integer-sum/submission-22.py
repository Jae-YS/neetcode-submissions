class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in sums:
                return [sums[diff], idx]
            else:
                sums[num] = idx
        return 