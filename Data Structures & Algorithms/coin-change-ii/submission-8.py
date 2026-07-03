class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case: 1 way to make 0
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill table
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for a in range(1, amount + 1):
                if a < coin:
                    dp[i][a] = dp[i - 1][a]          # can’t use this coin
                else:
                    dp[i][a] = dp[i - 1][a] + dp[i][a - coin]  # skip or use coin
        return dp[n][amount]