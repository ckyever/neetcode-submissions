# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        right_side_view = []
        queue = [root]

        while queue:
            right_side_view.append(queue[-1].val)
            # Process all nodes at the current tree depth
            for i in range(len(queue)):
                node = queue[i]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Remove them after otherwise above index won't work
            queue = queue[i+1:]
        
        return right_side_view

            