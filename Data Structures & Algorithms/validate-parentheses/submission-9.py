class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            "(": ")",
            "{": "}", 
            "[": "]"
        }

        for c in s:
            if c in check:
                stack.append(check[c])
            elif c not in check and not stack:
                return False
            elif stack.pop() != c:
                return False
        

        return True if len(stack) == 0 else False