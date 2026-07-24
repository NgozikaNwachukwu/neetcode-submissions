# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BASE CASE:
        # If root is None, we have moved past a leaf node.
        #
        # For example, a leaf node has:
        #
        #       7
        #      / \
        #   None None
        #
        # Calling invertTree(None) immediately returns.
        # This prevents the recursion from continuing forever.
        if not root:
            return None

        # SWAP THE CURRENT NODE'S CHILDREN.
        #
        # Before:
        #
        #       root
        #       /  \
        #    left  right
        #
        # Save the original left child so it is not lost.
        temp = root.left

        # Make the original right child the new left child.
        root.left = root.right

        # Make the original left child the new right child.
        root.right = temp

        # After:
        #
        #       root
        #       /  \
        #   right  left
        #
        # We only changed the two references belonging to `root`.
        # Each child brings its entire subtree with it.

        # RECURSIVE LEFT CALL:
        #
        # Invert the subtree that is NOW on the left.
        #
        # Important:
        # This is the original right subtree because we already swapped.
        #
        # The current function call pauses here until this entire
        # recursive call finishes.
        self.invertTree(root.left)

        # RECURSIVE RIGHT CALL:
        #
        # This line does not run until the left recursive call returns.
        #
        # Now invert the subtree that is on the right.
        # This is the original left subtree.
        self.invertTree(root.right)

        # Both subtrees have now been inverted.
        # Return the current node to the function call that called us.
        return root
        