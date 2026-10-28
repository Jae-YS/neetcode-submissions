class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, curr):
            if curr not in res:
                res.append(curr[:])
            
            if i > len(nums):
                return

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()

        backtrack(0, [])        
        return res