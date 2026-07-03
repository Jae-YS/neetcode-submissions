class Solution:

    def encode(self, strs: List[str]) -> str:
        retVal = []
        for word in strs:
            length = len(word)
            s = str(length) + "#" + word
            retVal.append(s)
        return "".join(retVal)

    def decode(self, s: str) -> List[str]:
        retVal = []
        l = 0
        print(s)
        while l < len(s):
            length = ""
            while s[l] != "#":
                length += s[l]
                l += 1
            r = l + int(length)

            retVal.append(s[l + 1: r + 1])
            l = r + 1
        return retVal
