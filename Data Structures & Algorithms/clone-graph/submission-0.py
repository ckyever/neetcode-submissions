"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeMap = {}

        def dfsCopy(node: Optional['Node']) -> Optional['Node']:
            if node in nodeMap:
                # Already made a copy of it
                return nodeMap[node]

            copy = Node(node.val)
            nodeMap[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfsCopy(neighbor))
            
            return copy

        return dfsCopy(node)