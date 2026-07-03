class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        prevRow = [0] * COLS
        prevRow[COLS - 1] = 1
        for i in range(ROWS - 1, -1, -1):
            curr = [0] * COLS
            checkRow = obstacleGrid[i]
            for l in range(COLS - 1, -1, -1):
                if l == COLS - 1:
                    curr[l] = 0 if checkRow[l] else prevRow[l]
                else:
                    curr[l] = 0 if checkRow[l] else curr[l + 1] + prevRow[l]
            
            prevRow = curr
            print(prevRow)
        return prevRow[0]