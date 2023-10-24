# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        if root is None:
            return
        queue = [root]
        product = []
        while queue:
            row_values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                row_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            product.append(max(row_values))
        return product
