class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        char_index = {}
        for idx, char in enumerate(word):
            char_index[char] = idx
           
        visited = []
        r, c = 0, 0
        ROWS, COLS = len(board), len(board[0])
        total = ROWS * COLS
        
        def go_through(r, c, idx):
            if (r, c) in visited: return False
            char = board[r][c]
            visited.append((r, c))

            if char == word[idx]:
                idx += 1 
                if idx == len(word):
                    return True
                top, left, right, bottom = False, False, False, False 
                
                if r != 0:
                    top = go_through(r - 1, c, idx)
                if c != 0:
                    left = go_through(r, c - 1, idx)
                if r < len(board) - 1:
                    bottom = go_through(r + 1, c, idx)
                if c < len(board[0]) - 1:
                    right = go_through(r, c + 1, idx)
                visited.remove((r, c))
                return top or bottom or right or left

            visited.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if go_through(r, c, 0):
                    return True


        
        return False