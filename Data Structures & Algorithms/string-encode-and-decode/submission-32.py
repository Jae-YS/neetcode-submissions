class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append(str(len(word)) + "#" + word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        retVal = []
        l = 0
        while l < len(s):
            j = l
            while s[j] != "#":
                j += 1
            length = s[l:j]
            l = j + int(length) + 1
            retVal.append(s[j + 1: l])
                
                
            
            



        return retVal