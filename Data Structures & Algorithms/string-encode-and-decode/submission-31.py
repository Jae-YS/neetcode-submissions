class Solution:

    def encode(self, strs: List[str]) -> str: 
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word  
        return s

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