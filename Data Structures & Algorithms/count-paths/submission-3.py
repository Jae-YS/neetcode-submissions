class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for i in range(m - 2, -1, -1):
            cur_row = [0] * n
            cur_row[n - 1] = 1
            for j in range(n - 2, -1, -1):
                cur_row[j] = cur_row[j + 1] + prev[j]
            
            prev = cur_row
        
        return prev[0]