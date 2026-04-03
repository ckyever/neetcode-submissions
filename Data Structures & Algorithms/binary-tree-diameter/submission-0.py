# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLongestBranch(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.getLongestBranch(root.left), self.getLongestBranch(root.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_diameter = self.getLongestBranch(root.left)
        right_diameter = self.getLongestBranch(root.right)
        max_diameter = max(left_diameter + right_diameter, self.diameterOfBinaryTree(root.left))
        max_diameter = max(max_diameter, self.diameterOfBinaryTree(root.right))

        return max_diameter


        
