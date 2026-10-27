class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = {}
        curr_length = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in dups: 
                dups[s[i]] = i 
            else:
                l = max(l, dups[s[i]] + 1)
                dups[s[i]] = i

            i += 1
            curr_length = max(curr_length, i - l)

        return curr_length
