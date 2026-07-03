from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])
        no_flip = set()

        r, c = 0, 0

        sides = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def check_sides(r, c):
            queue = deque([(r,c)])
            
            while queue:
                row, col = queue.popleft()
                if 0 <= row < ROWS and 0 <= col < COLS:

                    if board[row][col] == "O" and (row, col) not in no_flip:
                        no_flip.add((row, col))

                        for dx, dy in sides:
                            queue.append((row + dx, col + dy))
                    
        for r in range(ROWS):
            for c in [0, COLS-1]:  
                if board[r][c] == "O":
                    check_sides(r, c)

        for c in range(COLS):
            for r in [0, ROWS-1]:  
                if board[r][c] == "O":
                    check_sides(r, c)

        # flip rest
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == "O" and (r,c) not in no_flip:
                    board[r][c] = "X"
        
        
        


                