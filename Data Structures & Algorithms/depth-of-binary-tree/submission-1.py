# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case:
        #
        # If root is None, there is no node here.
        # An empty tree has a depth of 0.
        #
        # This is what stops the recursion.
        if not root:
            return 0

        # Find the maximum depth of the left subtree.
        #
        # The current function pauses while this recursive call runs.
        left_depth = self.maxDepth(root.left)

        # After the entire left subtree finishes,
        # find the maximum depth of the right subtree.
        right_depth = self.maxDepth(root.right)

        # Choose the deeper subtree.
        deeper_subtree = max(left_depth, right_depth)

        # Add 1 for the current node.
        return 1 + deeper_subtree