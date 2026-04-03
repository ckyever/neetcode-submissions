class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [node for node in range(n)] # index corresponds to node, value is it's parent
        sizes = [1] * n # index corresponds to node, value is the component size
        self.components = n

        def getRootParent(node: int) -> int:
            if node == parents[node]:
                # This is the root parent
                return node 
            
            parents[node] = getRootParent(parents[node])
            return parents[node]

        def unionGraph(root1: int, root2: int):
            bigGraph, smallGraph = root1, root2
            if sizes[root1] < sizes[root2]:
                bigGraph, smallGraph = root2, root1

            parents[smallGraph] = bigGraph
            sizes[bigGraph] = bigGraph + smallGraph
            self.components -= 1

        for node1, node2 in edges:
            root1 = getRootParent(node1)
            root2 = getRootParent(node2)
            if root1 != root2:
                unionGraph(root1, root2)

        return self.components
