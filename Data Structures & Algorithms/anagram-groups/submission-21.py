class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            buckets[key].append(word)
        return list(buckets.values())