class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        total = 0
        for token in tokens:
            if token in ops:
                b = numbers.pop()
                a = numbers.pop()
                numbers.append(ops[token](a, b))
            else:
                numbers.append(int(token))
        

        return numbers[-1]