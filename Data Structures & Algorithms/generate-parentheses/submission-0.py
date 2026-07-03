class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        para = []

        def backtrack(current, open_par, close_par):
            if len(current) == 2 * n:
                para.append(current)
                return
            
            if open_par < n:
                backtrack(current + "(", open_par + 1, close_par)
            
            if close_par < open_par:
                backtrack(current + ")", open_par, close_par + 1)

        if n > 0:
            backtrack("", 0, 0)
        
        return para