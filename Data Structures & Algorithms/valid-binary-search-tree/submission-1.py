# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we are defining a boundary for each node to determine if the node is part of a valid binary search
        # a BST is a tree that to the left subtree it has all values less than it, and in its right subtree it has all values greater than it.
        #surprisigly an empty tree is a valid BST
        # meaning as we are traversing through this tree recursively, we have to check, if this node is apart of the left subtree, is it between negative infinity and its parent node? and if its apart of the right subtree is this number between its parent node and positive infinity? IF WE TRAVERSE THROUGH THE ENTIRE TREE we are simply checking if each node passes this boundary correctly. 
        #since i will be using DFS, i will start with a helper function, traverse
        #we will call the left boundary left and right boundary right
        #since an empty tree can be a valid BST, this will be our base case

        def traverse(node, left, right):
        # BASE CASE: We reached the end of a branch (hit None).
        # This means we traversed a valid path without breaking any rules!
            if not node:
                return True 

        # ROOT/CURRENT NODE RANGE CHECK:
        # We ensure the current node strictly fits within the allowed bounds.
        # Checking just immediate left/right children isn't enough; 
        # we must check with reference to all its ancestors!
            if not (left < node.val < right): 
                return False

        # RECURSIVE STEP:
        # Once called, the child nodes become the new "local boss" (root).
        
        # 1. Going into the Left Subtree:
        # Everything down here MUST be smaller than "me" (the current node's value).
        # So "I" become its right boundary (upper ceiling).
        # It must still obey the floor ('left') set by previous ancestors.
            left_valid = traverse(node.left, left, node.val)
        
        # 2. Going into the Right Subtree:
        # Everything down here MUST be bigger than "me" (the current node's value).
        # So "I" become its left boundary (lower floor).
        # It must still obey the ceiling ('right') set by previous ancestors.
            right_valid = traverse(node.right, node.val, right)

        # Both subtrees must be perfectly valid for the whole tree to be valid.
            return left_valid and right_valid

    # KICKSTART: We start at the absolute root of the tree.
    # The initial floor is negative infinity, and the initial ceiling is positive infinity.
        return traverse(root, float("-inf"), float("inf"))

# =====================================================================
# INTERVIEW NOTES & COMPLEXITY:
# =====================================================================
# TIME COMPLEXITY: O(n)
# Why: We visit every single node exactly once. The boundary check inside 
# each call is a constant-time O(1) comparison operation.
#
# SPACE COMPLEXITY: O(h) where 'h' is the height of the tree.
# Why: It depends entirely on the recursive call stack. 
# - Balanced Tree Worst-Case: O(log n)
# - Skewed Tree (Linked-list style) Worst-Case: O(n)
# =====================================================================

        