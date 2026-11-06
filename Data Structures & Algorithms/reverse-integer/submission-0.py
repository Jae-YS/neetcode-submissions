class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            retVal = ["-"]
        else:
            retVal = []

        lb = -2**31
        ub = 2**31 - 1
        
        x = abs(x)
        x = str(x)
        retVal.extend(x[::-1])
        val = int("".join(retVal))
        if lb <= val <= ub:
            return val
        else:
            return 0