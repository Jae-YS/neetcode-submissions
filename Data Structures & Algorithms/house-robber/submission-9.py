class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[i], nums[0])
            else:
                val1 = nums[i] + dp[i -  2]
                val = dp[i - 1]
                dp[i] = max(val, val1)

        return max(dp)
