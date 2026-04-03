class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacencyMap = {node:[] for node in range(n)}

        for node1, node2 in edges:
            adjacencyMap[node1].append(node2)
            adjacencyMap[node2].append(node1)

        visited = set()
        def validateTreeWithDfs(current: int, previous: int) -> bool:
            if current in visited:
                return False

            visited.add(current)
            for neighbour in adjacencyMap[current]:
                if neighbour == previous:
                    continue
                if not validateTreeWithDfs(neighbour, current):
                    return False
        
            return True

        
        return validateTreeWithDfs(0, None) and len(visited) == n