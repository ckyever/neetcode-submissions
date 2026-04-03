class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        cols = []
        p_diagonals = []
        n_diagonals = []

        def dfs(board: List[List[str]], row: int):
            if row >= n:
                result.append(board.copy())
            
            for col in range(n):
                positive_diagonal = row + col
                negative_diagonal = row - col

                if (col not in cols and positive_diagonal not in p_diagonals and negative_diagonal not in n_diagonals):
                    # Generate row with queen placed
                    row_string = ""
                    for i in range(n):
                        if i == col:
                            row_string += 'Q'
                        else:
                            row_string += '.'
                    board.append(row_string)

                    # Mark indexes as used
                    cols.append(col)
                    p_diagonals.append(positive_diagonal)
                    n_diagonals.append(negative_diagonal)

                    # Place queen in the next row
                    dfs(board, row+1)

                    # Backtrack so remove queen before trying next decision path
                    board.pop()
                    cols.pop()
                    p_diagonals.pop()
                    n_diagonals.pop()
        
        dfs([], 0)

        return result
            
