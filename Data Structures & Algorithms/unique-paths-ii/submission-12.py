class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:        
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        prev = [0] * C
        prev[-1] = 1
        for i in range(R - 1, -1, -1):
            curr = [0] * C
            for j in range(C - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    curr[j] = 0
                else:
                    if j == C - 1:
                        curr[j] = prev[j]
                    else:
                        curr[j] = prev[j] + curr[j + 1]
            
            prev = curr
        return prev[0]
