class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        if amount == 0:
            return 0
        
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
        
        for i in range(len(dp)):
            for coin in coins:
                val = i - coin
                if val < 0:
                    continue
                else:
                    if dp[val] != float('inf'):
                        prev = dp[val]
                        dp[i] = min(dp[i], prev + 1)
        print(dp)
        return -1 if dp[-1] == float('inf') else dp[-1]