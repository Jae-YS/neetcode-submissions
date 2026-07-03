class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]
                if val == ".":
                    continue

                box_r = r // 3
                box_c = c // 3


                if val in rows[r] or val in cols[c] or val in boxes[box_r][box_c]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)

                boxes[box_r][box_c].add(val)

            
        
        return True

