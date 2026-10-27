class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        seen = set()
        

        def find_res(r,c):
            count = 0
            seen.add((r,c))
            queue = deque([(r,c)])
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while queue:
                x, y = queue.popleft()
                count += 1
                for dx, dy in dirs:
                    next_x = x + dx
                    next_y = y + dy

                    if (next_x, next_y) not in seen and next_x >= 0 and next_y >= 0 and next_x < ROW and next_y < COL and grid[next_x][next_y] == 1:
                        queue.append((next_x, next_y))
                        seen.add((next_x, next_y)) 
            return count

        

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen and grid[i][j] == 1:
                    area = max(area, find_res(i,j))
        
        return area