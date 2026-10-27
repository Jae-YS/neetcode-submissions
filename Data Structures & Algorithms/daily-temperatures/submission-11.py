class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        retVal = [0] * len(temperatures)
        stack = []
        for idx, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                stackt, stacki = stack.pop()
                retVal[stacki] = idx - stacki
            stack.append((num, idx))

        return retVal