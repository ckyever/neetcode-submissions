class Solution:
    def getPathKey(self, row: int, col: int) -> str:
        return f"{row},{col}"

    def exist(self, board: List[List[str]], word: str) -> bool:
        max_rows, max_cols = len(board), len(board[0])
        path = set()
        
        def dfs(row, col, i):
            if i == len(word):
                return True

            if (row < 0 or col < 0 
            or row >= max_rows or col >= max_cols 
            or word[i] != board[row][col] 
            or (row,col) in path):
                return False

            path.add((row, col))
            result = (dfs(row+1, col, i+1) or
                      dfs(row-1, col, i+1) or
                      dfs(row, col+1, i+1) or
                      dfs(row, col-1, i+1))
            
            path.remove((row,col))
            return result

        for row in range(max_rows):
            for col in range(max_cols):
                if dfs(row, col, 0):
                    return True

        return False 
