class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            total = 0
            while n > 9:
                num = n % 10
                total += num **2
                n //= 10
            total += n ** 2
            if total in seen:
                return False
            seen.add(total)
            n = total
            
        return True