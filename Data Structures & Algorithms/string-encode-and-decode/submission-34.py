class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            v = len(word) 
            s += str(v) + "#" + word
        return s

    def decode(self, s: str) -> List[str]:
        print(s)
        retVal = []

        l = r = 0
        while r < len(s):
            if s[r].isdigit():
                r += 1
            elif s[r] == "#":
                lens = int(s[l:r])
                word = s[r + 1: r + 1 + lens]
                retVal.append(word)
                l = r + 1 + lens
                r = l
            
             


        return retVal