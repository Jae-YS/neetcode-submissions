class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(len(nums)):
            if dp[i] == 1:
                c = i + 1
                check = nums[i]
                while c < len(nums) and check > 0:
                    dp[c] = 1
                    check -= 1
                    c += 1


        return dp[-1] == 1
