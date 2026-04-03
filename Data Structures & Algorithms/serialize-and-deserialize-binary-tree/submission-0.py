# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = ""
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            node_string = "None"
            if node:
                node_string = node.val
            serial += f"{node_string},"
            if node:
                queue.append(node.left if node else None)
                queue.append(node.right if node else None)
        
        return serial[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        deserialized_list = data.split(",")

        tree_list = []
        for string in deserialized_list:
            tree_list.append(None if string == "None" else int(string))
        
        if not tree_list[0]:
            return None

        root = TreeNode(tree_list[0])
        queue = collections.deque()
        queue.append(root)

        for i in range(1, len(tree_list)):
            if i % 2 == 0:
                node = queue.popleft()
                if tree_list[i]:
                    node.right = TreeNode(tree_list[i])
                    queue.append(node.right)
            else:
                if tree_list[i]:
                    queue[0].left = TreeNode(tree_list[i])
                    queue.append(queue[0].left)

        return root




