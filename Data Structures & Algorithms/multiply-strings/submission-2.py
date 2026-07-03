class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        
        def loop(num: str):
            total = 0
            length = len(num) - 1
            idx = 0
            while length >= 0:
                number = ord(num[idx]) - 48
                total += (10 ** length) * number
                length -= 1
                idx += 1 

            return total
        print(loop(num1))
        print(loop(num2))
        total = loop(num1) * loop(num2)
        return str(total)