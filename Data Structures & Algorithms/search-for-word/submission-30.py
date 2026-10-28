class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True

            elif r < 0 or c < 0 or r >= R or c >= C:
                return False
            if board[r][c] != word[i]: 
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            if (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)):
                return True
            
            board[r][c] = temp
            return False
            
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True

        return False