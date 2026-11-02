class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        cache = {}
        def is_pali(l, r):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            return s[l + 1:r]

        retVal = ""
        for i in range(len(s)):
            s1 = is_pali(i, i)
            s2 = is_pali(i-1, i)
            if len(s1) > len(retVal):
                retVal = s1
            elif len(s2) > len(retVal):
                retVal = s2
        
        return retVal

                


    