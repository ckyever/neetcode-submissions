class Solution:
    def solve(self, board: List[List[str]]) -> None:
        maxRows, maxCols = len(board), len(board[0])
        startingCells = []
        nonSurroundedOs = set()

        # All "O" on the board border are guaranteed not surrounded
        for r in range(maxRows):
            if board[r][0] == "O":
                    startingCells.append((r, 0))
                    nonSurroundedOs.add((r, 0))
            if board[r][maxCols-1] == "O":
                    startingCells.append((r, maxCols-1))
                    nonSurroundedOs.add((r, maxCols-1))

        for c in range(1, maxCols-1):
            if board[0][c] == "O":
                    startingCells.append((0, c))
                    nonSurroundedOs.add((0, c))
            if board[maxRows-1][c] == "O":
                    startingCells.append((maxRows-1, c))
                    nonSurroundedOs.add((maxRows-1, c))
                

        # Find all of the not surrounded "O" in the board by finding
        # any that are adjacent to the border ones
        for startRow, startCol in startingCells:
            queue = deque()
            queue.append((startRow, startCol))

            while queue:
                row, col = queue.popleft()

                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for translateRow, translateCol in directions:
                    newRow, newCol = row + translateRow, col + translateCol
                    if newRow < 0 or newRow >= maxRows or newCol < 0 or newCol >= maxCols:
                        continue

                    if board[newRow][newCol] == "O" and (newRow, newCol) not in nonSurroundedOs:
                        queue.append((newRow, newCol))
                        nonSurroundedOs.add((newRow, newCol)) 

        # Change all "O" that are surrounded
        for r in range(maxRows):
            for c in range(maxCols):
                if board[r][c] == "O" and (r, c) not in nonSurroundedOs:
                    board[r][c] = "X"