class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:        
        queue = deque()

        maxRows = len(grid)
        maxCols = len(grid[0])

        for r in range(maxRows):
            for c in range(maxCols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        currentSteps = 0
        while queue:
            nextQueue = deque()

            for row, col in queue:

                # Check each neighbouring cell
                for y, x in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

                    nextRow, nextCol = row+y, col+x
                    if nextRow < 0 or nextRow > maxRows-1 or nextCol < 0 or nextCol > maxCols-1:
                        # Move is out of bounds
                        continue
                    
                    nextCell = grid[nextRow][nextCol]

                    if nextCell != -1 and nextCell > currentSteps+1:
                        grid[nextRow][nextCol] = currentSteps + 1
                        nextQueue.append((nextRow, nextCol))

            queue = nextQueue
            currentSteps += 1 