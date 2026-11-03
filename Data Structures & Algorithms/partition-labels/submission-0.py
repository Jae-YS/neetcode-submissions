class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        l = r = 0
        char = s[0]
        count = freq[char]
        retVal = []
        keys = [char]
        
        while r < len(s):
            print(count)
            if s[r] in keys:
                count -= 1
                r += 1
            elif count == 0:
                retVal.append(r - l)
                l = r
                char = s[l]
                count = freq[char]
                keys = [char]
            else:
                keys.append(s[r])
                count += freq[s[r]] - 1
                r += 1
        retVal.append(r - l)

        return retVal