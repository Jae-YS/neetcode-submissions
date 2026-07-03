class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        for idx in range(1, len(nums)):
            left[idx] = left[idx - 1] * nums[idx -1]
        right = 1
        for idx in range(len(nums) - 1, -1, -1):
            left[idx] = left[idx] * right
            right = right * nums[idx]
        return left