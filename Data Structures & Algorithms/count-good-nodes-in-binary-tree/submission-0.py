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
            
            good_node = 0
            if root.val >= max_val:
                good_node += 1

            left_good_nodes = dfs(root.left, max(max_val, root.val))
            right_good_nodes = dfs(root.right, max(max_val, root.val)) 

            return left_good_nodes + right_good_nodes + good_node

        return dfs(root, root.val)
