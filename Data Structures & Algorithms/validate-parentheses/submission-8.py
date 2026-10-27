class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        val = {"(":")",
        "{":"}",
        "[":"]"}

        for char in s:
            if char in val:
                stack.append(val[char])
            elif stack and stack.pop() == char:
                continue
            else:
                return False

        return len(stack) == 0
