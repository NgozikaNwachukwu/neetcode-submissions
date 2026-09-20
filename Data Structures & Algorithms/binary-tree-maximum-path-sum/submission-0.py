# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #the whole point of the problem is, we are comparing the sum with a split(a node and its children) and without a split(a node with one singular line path of its left or right children(with no splits)) we create a leftsum and right sum, and we make sure to take the max between it and 0 to weed out negative nodes. at the end of the day, we want to return the max between left sum and right sum to the root and keeping track of the highest result we have seen so far
        # we do that by keeping the max result, ill start the result as the root node

        result = root.val

        def traverse(node):
            nonlocal result

            if not node:
                return 0

            leftMax = traverse(node.left) #max going left
            rightMax = traverse(node.right) #max going right
            leftMax = max(leftMax, 0) #to handle negative nodes
            rightMax = max(rightMax, 0) 
            #store the split in result incase the highest sum is here
            result = max(result, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        traverse(root)
        return result

            
        