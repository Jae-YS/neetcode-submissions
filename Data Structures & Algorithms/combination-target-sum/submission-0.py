class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(j, curr):
            if sum(curr) > target:
                return
            elif sum(curr) == target:
                res.append(curr[:])
            
            for i in range(j, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr)
                curr.pop()


        backtrack(0, [])
        return res