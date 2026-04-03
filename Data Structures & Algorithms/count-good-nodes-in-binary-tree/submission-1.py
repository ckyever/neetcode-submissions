# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, max_val: int) -> int:
            if not root:
                return 0
            
            good_nodes = 1 if root.val >= max_val else 0
            max_val = max(max_val, root.val)
            good_nodes += dfs(root.left, max_val)
            good_nodes += dfs(root.right, max_val) 

            return good_nodes

        return dfs(root, root.val)
