class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "+":
                val1 = stack[-1]
                val2 = stack[-2]
                total = val1 + val2
                stack.append(total)
            elif op == "D":
                val1 = stack[-1]
                total = 2 * val1 
                stack.append(total)
            else:
                stack.append(int(op))
        return sum(stack)
            