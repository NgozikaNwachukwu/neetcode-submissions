# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # dfs(node, maxVal) will return:
        # "the TOTAL number of good nodes in the subtree
        #  starting at this node"
        #
        # maxVal represents the MAXIMUM value we have seen
        # on the path from the original root to this node.
        #
        # Think of it as:
        #   maxVal travels DOWN the tree
        #   good-node counts (res) travel BACK UP the tree
        def dfs(node, maxVal):

            # BASE CASE:
            # If we have gone past a leaf and reached None,
            # there are no nodes here.
            #
            # Therefore this empty subtree contributes
            # 0 good nodes to our total.
            if not node:
                return 0


            # --------------------------------------------------
            # STEP 1: CHECK IF THE CURRENT NODE IS GOOD
            # --------------------------------------------------
            #
            # A node is "good" if its value is >= every value
            # we encountered on the path from the root to it.
            #
            # maxVal stores the largest value we have encountered
            # on that path so far.
            #
            # If current node >= maxVal:
            #     this node is good → count it → res = 1
            #
            # Otherwise:
            #     this node is not good → don't count it → res = 0
            #
            # So res initially represents ONLY whether the
            # CURRENT NODE should be counted.
            res = 1 if node.val >= maxVal else 0


            # --------------------------------------------------
            # STEP 2: UPDATE THE MAXIMUM FOR THE CHILDREN
            # --------------------------------------------------
            #
            # Before we travel farther down the tree, update
            # maxVal to include the current node.
            #
            # Example:
            #
            #       3
            #        \
            #         5
            #          \
            #           4
            #
            # At node 3:
            # maxVal = 3
            #
            # At node 5:
            # maxVal becomes 5
            #
            # When we eventually reach 4, we need to remember
            # that we previously encountered 5.
            #
            # Therefore 4 is NOT good because:
            # 4 < 5
            maxVal = max(maxVal, node.val)


            # --------------------------------------------------
            # STEP 3: COUNT GOOD NODES IN LEFT SUBTREE
            # --------------------------------------------------
            #
            # Recursively ask:
            #
            # "How many good nodes are in my LEFT subtree,
            #  given that maxVal is the largest value seen
            #  on the path so far?"
            #
            # IMPORTANT CALL STACK IDEA:
            #
            # The current dfs call PAUSES here while the recursive
            # call explores the left subtree.
            #
            # When that call eventually returns, it gives us
            # the NUMBER of good nodes it found.
            #
            # We add that number to res.
            res += dfs(node.left, maxVal)


            # --------------------------------------------------
            # STEP 4: COUNT GOOD NODES IN RIGHT SUBTREE
            # --------------------------------------------------
            #
            # Same exact idea for the right subtree.
            #
            # This recursive call returns the number of good
            # nodes found in the entire right subtree.
            #
            # Add that number to our running total.
            res += dfs(node.right, maxVal)


            # --------------------------------------------------
            # STEP 5: RETURN THE TOTAL FOR THIS ENTIRE SUBTREE
            # --------------------------------------------------
            #
            # At this point:
            #
            # res =
            #     current node (1 if good, 0 if not)
            #          +
            #     good nodes from left subtree
            #          +
            #     good nodes from right subtree
            #
            # In other words, this is the familiar recursive pattern:
            #
            #        ROOT + LEFT + RIGHT
            #
            # We return this number to the PREVIOUS recursive call,
            # which was paused waiting for us on the call stack.
            return res


        # ------------------------------------------------------
        # START THE RECURSION
        # ------------------------------------------------------
        #
        # Start at the root.
        #
        # We use root.val as our initial maxVal because there
        # are no ancestors above the root.
        #
        # This also means the root will always be considered good:
        #
        # root.val >= root.val → True
        #
        # dfs() will eventually return the total number of
        # good nodes in the ENTIRE tree.
        return dfs(root, root.val)
        