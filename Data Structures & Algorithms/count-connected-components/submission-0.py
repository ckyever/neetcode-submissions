class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyMap = {node:[] for node in range(n)}
        for a, b in edges:
            adjacencyMap[a].append(b)
            adjacencyMap[b].append(a)

        visited = set()
        components = 0

        while adjacencyMap:
            startNode = next(iter(adjacencyMap))

            def dfs(node: int):
                if node in visited:
                    return
                visited.add(node)

                for neighbour in adjacencyMap[node]:
                    dfs(neighbour)
                del adjacencyMap[node]

            dfs(startNode)
            components += 1
        
        return components