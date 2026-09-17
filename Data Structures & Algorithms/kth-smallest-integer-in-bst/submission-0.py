# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #my idea, using inorder DFS Traversal
        #think about it, in a BST, using inorder traversal, which is, going left, storing the value of the node then going right recursively, makes it in such a way that you store the left child, parent, THEN right vhild. and what does that do? TRAVERSE OUR TREE IN ASCENDING ORDER! and the question already told us the tree is BST to find the kth node
        count = 0
        def inorder(node):
            nonlocal count #python will complain abt using it in another function
            if not node:
                return None
            
            result = inorder(node.left) # stores the result of the calls from left subtree
            #this is a common technique. you ahevto store it somewhere! recursive calls will always return something so you need to store it or pythin will trash it.
            if result is not None:
                return result #if the left tree already found the answer return it!
            count += 1
            if count == k:
                return node.val
            
            return inorder(node.right)

        return inorder(root)
        