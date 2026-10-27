class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rqueue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rqueue.append((i,j))

        count = 0
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while rqueue and fresh > 0:
            n = len(rqueue)
            for _ in range(n):
                x, y = rqueue.popleft()
                for dx, dy in dirs:
                    next_x, next_y = x + dx, y + dy
                    if next_x >= 0 and next_y >= 0 and next_x < R and next_y < C and grid[next_x][next_y] == 1:
                        rqueue.append((next_x, next_y))
                        fresh -= 1
                        grid[next_x][next_y] = 2

            count += 1


        if fresh:
            return -1
        else:
            return count
        