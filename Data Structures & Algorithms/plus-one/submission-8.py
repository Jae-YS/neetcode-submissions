class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryOver = False
        for idx in range(len(digits) - 1, -1, -1):
            if idx == len(digits) - 1 or carryOver:
                val = digits[idx]
                val += 1
                if val == 10:
                    digits[idx] = 0
                    carryOver = True
                else:
                    digits[idx] += 1
                    return digits
        if carryOver:
            digits.insert(0, 1)
        return digits
                


