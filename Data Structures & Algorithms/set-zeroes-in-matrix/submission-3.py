class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        

        def set_val(r, c):
            row = matrix[r]
            for i in range(len(matrix)):
                if matrix[i][c] != 0:
                    matrix[i][c] = "*"
            
            for j in range(len(matrix[r])):
                if matrix[r][j] != 0:
                    matrix[r][j] = "*"

            return

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    set_val(r, c)
    
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        
        return