class Solution:
    def countSubstrings(self, s: str) -> int:
        l = 0
        pali = 0
        def isPali(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1 
            return True


        while l < len(s): 
            r = l + 1
            while r < len(s) + 1:
                if isPali(s[l:r]):
                    print(s[l:r])
                    pali += 1
                r += 1
            l += 1

        return pali