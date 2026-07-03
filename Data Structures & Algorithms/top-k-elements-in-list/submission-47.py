class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = set(nums)

        freq = {}
        for val in vals:
            freq[val] = nums.count(val)
        
        values = list(freq.items()) 
        sorted_vals = sorted(values, key=lambda x: x[1], reverse=True)
        ret_val = []
        print(sorted_vals)
        for i in range(k):
            ret_val.append(sorted_vals[i][0])
        return ret_val
