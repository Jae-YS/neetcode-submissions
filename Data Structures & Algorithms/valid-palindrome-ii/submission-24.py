class Solution:
    def validPalindrome(self, s: str) -> bool:

        c = ""
        for char in s:
            if char.isalnum():
                c += char.lower()
        
        l, r = 0, len(c) - 1
        while l < r:
            if c[l] != c[r]:
                break
            l += 1
            r -= 1

        if l >= r:
            return True 

        retVal = False
        for i in range(len(s)):
            t = c[0:i] + c[i + 1:]
            l, r = 0, len(t) - 1            
            while l < r:
                if t[l] != t[r]:
                    break
                l += 1
                r -= 1
            if l >= r:
                retVal = True
        return retVal