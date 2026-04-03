class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacencyMap = {}
        for node in range(n):
            adjacencyMap[node] = []

        for fromNode, toNode in edges:
            adjacencyMap[fromNode].append(toNode)
            adjacencyMap[toNode].append(fromNode)

        visited = set()
        def validateTreeWithDfs(current: int, previous: int) -> bool:
            if current in visited:
                return False

            visited.add(current)
            for neighbour in adjacencyMap[current]:
                if neighbour != previous:
                    if not validateTreeWithDfs(neighbour, current):
                        return False
            
            return True

        
        return validateTreeWithDfs(0, None) and len(visited) == n