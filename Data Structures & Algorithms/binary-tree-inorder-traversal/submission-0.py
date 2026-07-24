# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        def traverse(node):
            if not node:
                return
            if node.left is not None:
                traverse(node.left)
            results.append(node.val)
            if node.right is not None:
                traverse(node.right)
        traverse(root) # REMEMEBER WE NEED TO CALL THE TRAVERSE METHOD FOR THE ROOT
        return results
        