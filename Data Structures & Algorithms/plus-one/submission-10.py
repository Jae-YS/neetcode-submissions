class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry and i >= 0:
            val = digits[i]
            val += 1
            if val < 10:
                carry = False
            val %= 10
            digits[i] = val
            i -= 1
        
        if carry:
            return [1] + digits
        
        return digits


        
        

        
        