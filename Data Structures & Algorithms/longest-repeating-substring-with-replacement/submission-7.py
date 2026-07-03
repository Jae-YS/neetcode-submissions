class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        best = 0
        max_freq = 0

        for i in range(len(s)):
            count[ord(s[i]) - ord('A')] += 1
            max_freq = max(count)

            while (i - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            best = max(best, i - left + 1 )


        

        return best

