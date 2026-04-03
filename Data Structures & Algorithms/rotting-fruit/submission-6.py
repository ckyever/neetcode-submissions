class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        maxRows, maxCols = len(grid), len(grid[0])

        visited = set()
        rottenQueue = deque()
        self.freshFruit = 0

        for row in range(maxRows):
            for col in range(maxCols):
                if grid[row][col] == 1:
                    self.freshFruit += 1
                if grid[row][col] == 2:
                    rottenQueue.append((row, col))
                    visited.add((row, col))

        if self.freshFruit == 0:
            return 0

        def spread(row: int, col: int):
            if (row, col) in visited:
                return

            if row >= 0 and row < maxRows and col >= 0 and col < maxCols:
                if grid[row][col] == 1:
                    visited.add((row, col))
                    self.freshFruit -= 1
                    rottenQueue.append((row, col))

        minutes = 0
        while rottenQueue:
            minutes += 1
            prevFreshFruit = self.freshFruit

            for _ in range(len(rottenQueue)):
                row, col = rottenQueue.popleft()
                spread(row - 1, col)
                spread(row + 1, col)
                spread(row, col - 1)
                spread(row, col + 1)
            
            if prevFreshFruit > 0 and prevFreshFruit == self.freshFruit:
                # We still have fresh fruit and the rotten ones have stopped spreading
                # so there is no solution
                return -1
        
        return minutes-1
                