class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(dp)):
            if dp[i] == 1:
                curr = s[i:]
                for word in wordDict:
                    if curr.startswith(word):
                        w = len(word)
                        if i + w < len(dp):
                            dp[i + w] = 1
                
        return dp[-1] == 1

