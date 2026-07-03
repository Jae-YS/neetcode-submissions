class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        prevRow = [0] * COLS
        for i in range(m - 1, -1, -1):
            curr = [0] * COLS
            curr[COLS - 1] = 1
            for l in range(n - 2, -1, -1):
                curr[l] = curr[l + 1] + prevRow[l]

            prevRow = curr

        return prevRow[0]