class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        VISITED = -1
        LAND = 1

        maxArea = 0
        gridRows = len(grid)
        gridCols = len(grid[0])

        for row in range(gridRows):
            for col in range(gridCols):
                cell = grid[row][col]

                if cell == VISITED:
                    continue

                if cell == LAND:
                    # Explore all of this island with BFS
                    queue = deque([(row, col)])
                    islandArea = 0
                    while queue:
                        visitRow, visitCol = queue.popleft()
                        if grid[visitRow][visitCol] == LAND:
                            islandArea += 1
                            # Checking each direction
                            for rowTranslate, colTranslate in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                nextRow = visitRow + rowTranslate
                                nextCol = visitCol + colTranslate

                                # Only explore if it is in the grid boundaries
                                if nextRow in range(gridRows) and nextCol in range(gridCols):
                                    queue.append((nextRow, nextCol))

                            grid[visitRow][visitCol] = VISITED

                    # Check if this island is the biggest so far
                    maxArea = max(maxArea, islandArea)
                
                grid[row][col] = VISITED
        
        return maxArea