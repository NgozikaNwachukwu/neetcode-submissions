# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True

        if not s: # if s is empty but t is non empty
            return False
        
        if self.sameTree(s, t):
            return True # checking starting from the root

        # we can compare t to the left subtree of s and right subtree of s
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))


    def sameTree(self, s, t):
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                self.sameTree(s.right, t.right))

        return False # if one is empty and one is none empty
            
        