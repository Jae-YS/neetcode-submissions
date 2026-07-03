from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        sides = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def to_check(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                if 0 <= r < ROWS and 0 <= c < COLS:

                    if grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r,c))
                        for dx, dy in sides:
                            queue.append((r + dx, c + dy))


        island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island += 1 
                    to_check(r, c)
        
        return island