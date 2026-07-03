class Solution:
    def isValid(self, s: str) -> bool:
        opp = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for char in s:
            
            if char in opp:
                stack.append(opp[char])
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False