class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(s) != set(t):
            return False
        letters = set(s)
        for char in letters:
            if s.count(char) != t.count(char):
                return False
            
        return True