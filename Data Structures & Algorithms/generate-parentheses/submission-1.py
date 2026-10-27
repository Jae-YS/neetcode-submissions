class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, stack):
            if len(curr) == n * 2 and len(stack) == 0:
                val = "".join(curr)
                res.append(val)
                return
            if len(stack) > n or len(curr) > n * 2:
                return

            curr.append("(")
            stack.append("(")
            backtrack(curr, stack)
            curr.pop()
            stack.pop()
            if stack:
                curr.append(")")
                stack.pop()
                backtrack(curr, stack)
                stack.append("(")
                curr.pop()
                    

        backtrack([], [])
        return res