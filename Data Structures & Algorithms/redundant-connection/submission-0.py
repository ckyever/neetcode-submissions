class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = len(edges)

        parents = []
        sizes = []
        for n in range(nodes+1):
            parents.append(n)
            sizes.append(1)

        def getRoot(node: int) -> int:
            if parents[node] == node:
                return node

            parents[node] = getRoot(parents[node])
            return parents[node]

        def union(root1: int, root2: int):
            smallGraph, largeGraph = root1, root2

            if sizes[root1] > sizes[root2]:
                smallGraph, largeGraph = root2, root1

            parents[smallGraph] = parents[largeGraph]
            sizes[largeGraph] += sizes[smallGraph]

        for node1, node2 in edges:
            root1, root2 = getRoot(node1), getRoot(node2)

            if root1 == root2:
                return [node1, node2]
            else:
                union(root1, root2)

        raise Exception("This graph does not have a solution")