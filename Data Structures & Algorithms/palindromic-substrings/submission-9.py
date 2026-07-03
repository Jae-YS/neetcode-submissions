class Solution:
    def countSubstrings(self, s: str) -> int:
        l = 0
        pali = 0
        def isPali(i: int, j: int) -> bool:
            l, r = i, j - 1
            while l < r and s[l] == s[r]:
                l += 1; r -= 1
            return l >= r



        while l < len(s): 
            r = l + 1
            while r < len(s) + 1:
                if isPali(l, r):
                    pali += 1
                r += 1
            l += 1
        return pali