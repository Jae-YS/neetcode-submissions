class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                square = board[r][c]
                if square == ".":
                    continue
                board_row = r // 3
                board_col = c // 3

                if square in rows[r] or square in cols[c] or square in box[board_row][board_col]:
                    return False
                
                rows[r].add(square)
                cols[c].add(square)
                box[board_row][board_col].add(square)
        
        return True