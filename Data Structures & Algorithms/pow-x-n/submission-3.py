class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x: float, n: int) -> float:
            if n == 0:
                return 1.0
            
            half = calculate(x, n // 2)
            
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        res = calculate(x, abs(n))
        
        return 1 / res if n < 0 else res