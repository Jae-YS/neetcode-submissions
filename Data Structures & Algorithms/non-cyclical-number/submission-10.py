class Solution:
    def isHappy(self, n: int) -> bool:
        def f(x: int) -> int:
            return sum(int(digit)**2 for digit in str(x))

        slow = f(n)
        fast = f(f(n))

        while slow != fast:
            slow = f(slow)       
            fast = f(f(fast))    

        return slow == 1
