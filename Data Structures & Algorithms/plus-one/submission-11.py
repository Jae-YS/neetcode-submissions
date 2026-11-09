class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry and i > -1:
            val = digits[i] + 1
            if val < 10:
                carry = False

            digits[i] = val % 10
            i -= 1     
        

        if carry:
            return [1] + digits
        else:
            return digits