class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        VISITED = 'V'
        LAND = '1'

        height = len(grid)
        width = len(grid[0])

        def isValidPosition(row: int, col: int) -> bool:
            if row >= 0 and row < height and col >= 0 and col < width:
                return True

            return False

        islandCount = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == VISITED:
                    continue

                if grid[row][col] == LAND:
                    queue = [(row, col)]
                    while queue:
                        toVisitRow, toVisitCol = queue.pop()

                        if grid[toVisitRow][toVisitCol] == VISITED:
                            continue

                        # Check top cell
                        if isValidPosition(toVisitRow - 1, toVisitCol):
                            if grid[toVisitRow - 1][toVisitCol] == LAND:
                                queue.append((toVisitRow - 1, toVisitCol))
                            else:
                                grid[toVisitRow - 1][toVisitCol] = VISITED

                        # Check right cell
                        if isValidPosition(toVisitRow, toVisitCol + 1):
                            if grid[toVisitRow][toVisitCol + 1] == LAND:
                                queue.append((toVisitRow, toVisitCol + 1))
                            else:
                                grid[toVisitRow][toVisitCol + 1] = VISITED

                        # Check bottom cell
                        if isValidPosition(toVisitRow + 1, toVisitCol):
                            if grid[toVisitRow + 1][toVisitCol] == LAND:
                                queue.append((toVisitRow + 1, toVisitCol))
                            else:
                                grid[toVisitRow + 1][toVisitCol] = VISITED

                        # Check left cell
                        if isValidPosition(toVisitRow, toVisitCol - 1):
                            if grid[toVisitRow][toVisitCol - 1] == LAND:
                                queue.append((toVisitRow, toVisitCol - 1))
                            else:
                                grid[toVisitRow][toVisitCol - 1] = VISITED

                        grid[toVisitRow][toVisitCol] = VISITED
                    
                    islandCount += 1
                
                else:
                    # This is water
                    grid[row][col] = VISITED
        
        return islandCount