class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        string = ""
        while columnNumber > 0:
            columnNumber -= 1 
            val = columnNumber % 26
            string += chr(val + 65)
            columnNumber = columnNumber // 26

        return string[::-1]