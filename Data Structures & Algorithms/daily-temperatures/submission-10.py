class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        retVal = [0] * len(temperatures)
        stack = []
        for idx, num in enumerate(temperatures):
            if not stack:
                stack.append((num, idx))
            else:
                (prev_temp, i) = stack[-1]
                while num > prev_temp and stack:
                    retVal[i] = idx - i
                    stack.pop()
                    if stack:
                        prev_temp, i = stack[-1]
                stack.append((num, idx))

        return retVal