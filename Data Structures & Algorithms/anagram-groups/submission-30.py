class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        types = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            types[key].append(word)
        
        retVal = []
        for value in types.values():
            retVal.append(value)
        
        return retVal

