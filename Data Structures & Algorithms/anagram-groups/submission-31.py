class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        types = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            types[tuple(count)].append(word)
        
        retVal = []
        for value in types.values():
            retVal.append(value)
        
        return retVal

