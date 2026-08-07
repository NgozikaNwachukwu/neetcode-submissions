# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root # curr is a pointer

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right # if theyre both greater go down right subtree since this is a BST
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left #go down left subtree
            else:
                return cur
        