class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        R, C = len(grid), len(grid[0])
        queue = deque()

        # Step 1: Add all treasure chests (0) to the queue as starting points
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c))

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Step 2: Multi-source BFS outwards
        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                # Only visit valid empty land cells (INF / 2147483647)
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))