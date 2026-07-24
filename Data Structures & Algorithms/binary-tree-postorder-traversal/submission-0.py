# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []

        def traverse(node):
            if not node:
                return
            
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
            results.append(node.val)

        traverse(root)
        return results
        