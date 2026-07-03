class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i, char in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
        return strs[0]