class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]
            k = i
            curr = float('inf')
            for j in range(1,val + 1):
                if k + j < len(dp):
                    curr = min(curr, dp[k + j] + 1)
            dp[i] = curr 


                


        return dp[0]
        