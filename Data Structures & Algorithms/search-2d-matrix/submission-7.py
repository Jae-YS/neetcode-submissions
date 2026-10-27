class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R = len(matrix)

        l, r = 0, R - 1
        curr = -1
        while l <= r:
            m = (l + r) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                curr = m
                break
        
        row = matrix[curr]

        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
        