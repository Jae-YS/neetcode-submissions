class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = ""
        for c in s:
            if c.isalnum():
                val += c.lower()
        print(val)
        l, r = 0, len(val) - 1

        while l < r:
            if val[l] != val[r]:
                return False
            l +=1 
            r -=1
        return True 