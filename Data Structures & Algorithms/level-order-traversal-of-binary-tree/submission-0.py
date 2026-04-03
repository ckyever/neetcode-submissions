# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []
        def dfs(root: Optional[TreeNode], depth) -> int:
            if not root:
                return depth - 1
            
            if len(self.result) <= depth:
                self.result.append([root.val])
            else:
                self.result[depth].append(root.val)

            dfs(root.left, depth + 1)
            return dfs(root.right, depth + 1)
            
        dfs(root, 0)
        return self.result
