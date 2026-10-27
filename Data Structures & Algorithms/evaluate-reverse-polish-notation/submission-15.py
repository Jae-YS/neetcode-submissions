class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "*", "/"]
        total = 0
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                val2 = stack.pop()
                val1 = stack.pop()
                res = 0
                if token == "+":
                    res = val1 + val2
                elif token == "-":
                    res = val1 - val2
                elif token == "*":
                    res = val1 * val2
                else:
                    res = val1 / val2
                
                stack.append(int(res))


        return stack.pop()
                
        
            