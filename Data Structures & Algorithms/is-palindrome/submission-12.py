class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ""
        for char in s:
            if char.isalnum():
                clean_str += char.lower()

        l, r = 0, len(clean_str) - 1
        while l < r:
            if clean_str[l] != clean_str[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
