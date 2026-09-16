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
            if not node:
                return True # our base case

            #we need to check if this node fits our boundary

            #if node.left > left and node.left < node.val
            #if node.right > node.val and node.right < right
            if not(left < node.val < right): #WE NEED TO CHECK THE ROOT! CHECK THAT THE ROOT IS WITHIN RANGE.
                return False


            return (traverse(node.left, left, node.val) and
            traverse(node.right, node.val, right))

        return traverse(root, float("-inf"), float("inf"))

        