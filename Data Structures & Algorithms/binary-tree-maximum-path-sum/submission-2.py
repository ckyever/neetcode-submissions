# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mps = root.val

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            best_left_path = max(left, 0)
            best_right_path = max(right, 0)
            best_split_path = root.val + best_left_path + best_right_path

            self.mps = max(self.mps, best_split_path)

            return root.val + max(best_left_path, best_right_path)

        dfs(root)

        return self.mps