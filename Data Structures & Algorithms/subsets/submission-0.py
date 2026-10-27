class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def backtrack(curr, start):
            

            for i in range(start, len(nums)):
                curr.append(nums[i])
                res.append(curr[:])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return res