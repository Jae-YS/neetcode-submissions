class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(val, curr, j):
            if val == target:
                res.append(curr[:])
                return
            if val > target:
                return

            for i in range(j, len(candidates)):
                if i > j and candidates[i] == candidates[i - 1]:
                    continue
                curr.append(candidates[i])
                val += candidates[i]
                backtrack(val, curr, i + 1)
                curr.pop()
                val -= candidates[i]
        
        backtrack(0, [], 0)
        return res