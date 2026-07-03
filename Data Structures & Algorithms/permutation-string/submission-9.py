class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        if n > m: 
            return False
        
        def idx(c):
            return ord(c) - ord('a')
        
        need = [0] * 26
        have = [0] * 26

        for char in s1:
            char_idx = idx(char)
            need[char_idx] += 1

        for char in s2[:n]:
            char_idx = idx(char)
            have[char_idx] += 1
        
        if need == have:
            return True
        
        for r in range(n, m):
            add = idx(s2[r])
            rem = idx(s2[r - n])

            have[add] += 1
            have[rem] -= 1

            if need == have:
                return True
        return False


        
