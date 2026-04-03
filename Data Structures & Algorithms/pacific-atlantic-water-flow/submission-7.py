class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        maxRows, maxCols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        for row in range(maxRows):
            pacific.add((row, 0))
            atlantic.add((row, maxCols-1))

        for col in range(maxCols):
            pacific.add((0, col))
            atlantic.add((maxRows-1, col))

        def bfs(oceanCoords):
            startCells = list(oceanCoords)
            for startRow, startCol in startCells:
                queue = deque()
                queue.append((startRow, startCol))
                while queue:
                    row, col = queue.popleft()
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for translateRow, translateCol in directions:
                        newRow, newCol = row + translateRow, col + translateCol
                        if (newRow, newCol) in oceanCoords:
                            continue
                        if newRow >= 0 and newRow < maxRows and newCol >= 0 and newCol < maxCols:
                            if heights[newRow][newCol] >= heights[row][col]:
                                queue.append((newRow, newCol))
                                oceanCoords.add((newRow, newCol))
        
        bfs(pacific)
        bfs(atlantic)

        pacificAtlantic = pacific.intersection(atlantic)

        result = []
        for row, col in pacificAtlantic:
            result.append([row, col])
        
        return result   