class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        freq1 = Counter(s1)

        while r < len(s2) + 1:
            sub_s2 = s2[l:r]
            print(sub_s2)
            if freq1 == Counter(sub_s2):
                return True
            l += 1
            r += 1
        
        return False
