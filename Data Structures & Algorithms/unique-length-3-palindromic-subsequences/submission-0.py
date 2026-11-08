class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        char_idx = {}
        for i in range(len(s)):
            if s[i] not in char_idx:
                char_idx[s[i]] = [i, i]
            else:
                char_idx[s[i]][1] = i



        count = 0
        for char in set(s):
            fst, lst = char_idx[char]
            if lst - fst < 2:
                continue
            count += len(set(s[fst + 1: lst]))
        return count
        