class Solution:
    def validPalindrome(self, s: str) -> bool:

        c = ""
        for char in s:
            if char.isalnum():
                c += char.lower()

        l, r = 0, len(c) - 1

        def palindrome(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True


        def check(l, r):
            # remove left
            word = s[0:l] + s[l + 1:]
            val = palindrome(word)
            if val:
                return True
            word = s[0:r] + s[r + 1:]
            val = palindrome(word)
            if val:
                return True
            return False
        
        if palindrome(c):
            return True
        else:
            while l < r: 
                if c[l] != c[r]:
                    val = check(l, r)
                    if val:
                        return True
                    else:
                        return False
                l += 1
                r -= 1
            return False