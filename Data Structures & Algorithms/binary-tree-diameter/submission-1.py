# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Stores the largest diameter found anywhere in the tree.
        #
        # The diameter is measured in edges.
        #
        # We use a shared variable because dfs() needs to return height
        # to the parent, while we separately keep track of the best
        # diameter found across all nodes.
        self.res = 0

        def dfs(curr):
            """
            Returns the height of the subtree rooted at curr.

            While calculating heights, every node also checks the
            diameter that would pass through itself.

            Important distinction:

            - dfs(curr) RETURNS height.
            - self.res STORES the largest diameter found so far.
            """

            # An empty subtree has height 0.
            #
            # This allows leaf nodes to receive:
            # left_height = 0
            # right_height = 0
            if not curr:
                return 0

            # Recursively ask the left child:
            # "What is the height of your subtree?"
            left_height = dfs(curr.left)

            # Recursively ask the right child:
            # "What is the height of your subtree?"
            right_height = dfs(curr.right)

            # The longest path passing through the current node uses:
            #
            # 1. The deepest path in the left subtree
            # 2. The deepest path in the right subtree
            #
            # Therefore:
            #
            # diameter through curr
            # = left height + right height
            #
            # Example:
            #
            #       curr
            #       /  \
            #   left    right
            #
            # If left_height = 2 and right_height = 3,
            # the path through curr has 2 + 3 = 5 edges.
            diameter_through_curr = left_height + right_height

            # Every node checks whether the diameter passing through
            # itself is larger than the best diameter found previously.
            #
            # This is how the solution handles the fact that the largest
            # diameter may not pass through the original root.
            self.res = max(self.res, diameter_through_curr)

            # Return the height of the current subtree to curr's parent.
            #
            # A path going upward to the parent can only continue through
            # one side of curr:
            #
            # either the left side or the right side,
            # whichever is taller.
            #
            # We add 1 to include the current node.
            return 1 + max(left_height, right_height)

        # Start the depth-first search from the original root.
        #
        # We do not use the value returned here because it represents
        # the height of the entire tree, not the diameter.
        dfs(root)

        # After every node has checked its own possible diameter,
        # self.res contains the largest diameter found anywhere.
        return self.res
        