class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        val = 1
        TOP = LEFT = 0
        BOTTOM = RIGHT = n
        i = j = 0
        while val <= n ** 2:
            while j < RIGHT:
                matrix[i][j] = val
                val += 1
                j += 1
            
            j -= 1
            i += 1
            TOP += 1

            while i < BOTTOM:
                matrix[i][j] = val
                val += 1
                i += 1
            
            RIGHT -= 1
            i -= 1
            j -= 1

            while j >= LEFT:
                matrix[i][j] = val
                val += 1
                j -= 1
            
            j += 1
            i -= 1
            BOTTOM -= 1

            while i >= TOP:
                matrix[i][j] = val
                val += 1
                i -= 1
            
            i += 1
            j += 1
            LEFT += 1

        return matrix




