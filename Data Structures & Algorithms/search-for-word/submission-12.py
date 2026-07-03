class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:           
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
        def go_through(r, c, idx):
            if (r, c) in visited: return False
            if board[r][c] != word[idx]: return False
            
            visited.add((r, c))
            idx += 1 
                
            if idx == len(word):
                return True

            res = False    
            if r > 0:
                res = res or go_through(r - 1, c, idx)
            if c > 0:
                res = res or go_through(r, c - 1, idx)
            if r < ROWS - 1:
                res = res or go_through(r + 1, c, idx)
            if c < COLS - 1:
                res = res or go_through(r, c + 1, idx)
            visited.remove((r, c))
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if go_through(r, c, 0):
                    return True


        
        return False