class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for word in strs[1:]:
            if len(shortest) > len(word):
                shortest = word
        
        l, r = 0, len(shortest)

        while l <= r:
            curr = shortest[0:l]
            print(curr)
            for word in strs:
                if curr not in word:
                    return shortest[0:l-1]
            l += 1
        return shortest