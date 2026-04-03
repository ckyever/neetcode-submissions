class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        VISITED = -1
        LAND = 1

        maxArea = 0
        gridRows = len(grid)
        gridCols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= gridRows or col < 0 or col >= gridCols or grid[row][col] != LAND:
                return 0

            grid[row][col] = VISITED
            area = 1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1)
            return area

        for row in range(gridRows):
            for col in range(gridCols):
                if grid[row][col] == VISITED:
                    continue

                if grid[row][col] == LAND:
                    maxArea = max(maxArea, dfs(row, col))
                
                grid[row][col] == VISITED
                
        return maxArea