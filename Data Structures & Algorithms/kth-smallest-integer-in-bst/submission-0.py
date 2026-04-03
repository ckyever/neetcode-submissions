# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.jumps_left = k
        self.kth_value = None

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            dfs(root.left)

            self.jumps_left -= 1
            if self.jumps_left == 0:
                self.kth_value = root.val
                return

            dfs(root.right)

            return
        dfs(root)
        
        return self.kth_value