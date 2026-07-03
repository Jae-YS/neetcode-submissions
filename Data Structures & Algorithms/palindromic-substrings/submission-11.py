class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [False] * n
        count = 0

        for i in range(n - 1, -1, -1):
            prev = False
            for j in range(i, n):
                temp = dp[j]
                if s[i] == s[j] and (j - i < 2 or prev):
                    dp[j] = True
                    count += 1
                else:
                    dp[j] = False
                prev = temp
        return count
