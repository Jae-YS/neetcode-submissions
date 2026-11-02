class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1
        dp[1] = 1

                
        for i in range(1, len(s)):
            num1 = int(s[i - 1: i + 1])
            num2 = int(s[i])
            if num1 <= 26 and num1 > 9 and s[i - 1] != "0":
                dp[i + 1] += dp[i - 1]
            if num2 > 0:
                dp[i+ 1] += dp[i]

        
        return dp[-1]
                

            