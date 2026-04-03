# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], left_bound: int, right_bound: int) -> bool:
            if not root:
                return True

            if root.val <= left_bound or root.val >= right_bound:
                return False

            is_left_subtree_valid = dfs(root.left, left_bound, root.val)
            is_right_subtree_valid = dfs(root.right, root.val, right_bound)

            return is_left_subtree_valid and is_right_subtree_valid

        return dfs(root, -math.inf, math.inf)