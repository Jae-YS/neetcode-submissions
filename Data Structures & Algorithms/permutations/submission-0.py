class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, j):
            if len(curr) == len(nums):
                res.append(curr[:])
            
            for i in range(len(nums)):
                if i not in j:
                    curr.append(nums[i])
                    j.append(i)
                    backtrack(curr, j)
                    j.pop()
                    curr.pop()
            

        backtrack([], [])
        return res