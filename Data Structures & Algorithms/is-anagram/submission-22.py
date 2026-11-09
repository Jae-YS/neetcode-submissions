class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars = set(s)
        for c in chars:
            if s.count(c) != t.count(c):
                return False
        return True