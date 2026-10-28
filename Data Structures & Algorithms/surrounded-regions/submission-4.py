class Solution:
    def solve(self, board: List[List[str]]) -> None:
            
        ROW, COL = len(board), len(board[0])
        seen = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def flip(r,c):
            stack = [(r,c)]
            while stack:
                x, y = stack.pop()
                seen.add((r,c))
                board[x][y] = "Z"
                for dx, dy in dirs:
                    next_x, next_y = x + dx, y + dy
                    if next_x > -1 and next_y > -1 and next_x < ROW and next_y < COL and board[next_x][next_y] == "O":
                        stack.append((next_x, next_y))



        for j in range(COL):
            if board[0][j] == "O":
                flip(0, j)

        for i in range(1, ROW):
            if board[i][COL - 1] == "O": 
                flip(i, COL - 1)

        if ROW > 1:
            for j in range(COL - 2, -1, -1):
                if board[ROW - 1][j] == "O":
                    flip(ROW - 1, j)

        if COL > 1:
            for i in range(ROW - 2, 0, -1):
                if board[i][0] == "O":
                    flip(i, 0)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"
        
        return