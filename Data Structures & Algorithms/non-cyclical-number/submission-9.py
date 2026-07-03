class Solution:
    def isHappy(self, n: int) -> bool:

        def total(n: int) -> int:
            add = 0
            while n > 0:
                val = n % 10
                add += val * val
                n = n // 10
            return add
                
        seen = set()
        while n != 1:
            total_sum = total(n)
            if total_sum in seen:
                return False
            else:
                seen.add(total_sum)
            n = total_sum 
        return True