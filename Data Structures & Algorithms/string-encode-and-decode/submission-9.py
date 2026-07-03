class Solution:

    def encode(self, strs: List[str]) -> str:
        retVal = ""

        for s in strs:
            length = len(s)
            retVal += str(length) + "#" + s
        print(retVal)
        return retVal

    def decode(self, s: str) -> List[str]:
        retVal = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = s[i:j]
            i = j + int(length) + 1
            retVal.append(s[j + 1: i])
        return retVal
        