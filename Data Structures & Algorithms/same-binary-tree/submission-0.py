# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSame = True

        def bfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p == None and q == None:
                return

            if p == None or q == None:
                # They must be different
                self.isSame = False
                return

            if p.val != q.val:
                self.isSame = False
                return

            bfs(p.left, q.left)
            bfs(p.right, q.right)
        
        bfs(p, q)
        return self.isSame