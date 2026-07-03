class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = set(nums)
        freq = {}

        for val in vals:
            freq[val] = nums.count(val)

        freq = list(freq.items())
        freq.sort(key=lambda x: x[1], reverse=True)
        print(freq)
        retVal = []
        for i in range(k):
            retVal.append(freq[i][0]) 
        return retVal
