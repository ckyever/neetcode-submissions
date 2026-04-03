"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First loop through head
            # Create new node and add to hashmap where original node is key and new node is value
        
        # Second loop through head
            # By referencing hashmap
            # Set next and random of copy 

        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            node_map[current].next = node_map.get(current.next, None)
            node_map[current].random = node_map.get(current.random, None)
            current = current.next

        return node_map.get(head, None)