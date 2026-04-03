# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                # Not balanced so stop the search
                self.isBalanced = False
                return -1

            return max(left, right) + 1
            
        dfs(root)
        return self.isBalanced