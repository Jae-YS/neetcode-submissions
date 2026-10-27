class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_len, s1_len = len(s2), len(s1)
        if s1_len > s2_len:
            return False
        s1_freq = [0] * 26
        s2_window_freq = [0] * 26
        
        for i in range(s1_len):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_window_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == s2_window_freq:
                return True

        for j in range(s2_len - s1_len):
            s2_window_freq[ord(s2[j]) - ord('a')] -= 1
            s2_window_freq[ord(s2[j + s1_len]) - ord('a')] += 1
            if s2_window_freq == s1_freq:
                return True

        return False