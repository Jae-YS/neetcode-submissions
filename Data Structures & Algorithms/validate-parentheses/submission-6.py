class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        for bracket in s:
            if bracket in brackets:
                stack.append(brackets[bracket])
            else: 
                if stack and stack.pop() == bracket:
                    continue
                else:
                    return False
            
        

        return len(stack) == 0
