# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # BASE CASE:
        # If root is None, we have reached an empty subtree.
        #
        # This usually means one of two things:
        # 1. The key does not exist along this search path, OR
        # 2. A recursive call has reached past the end of the tree.
        #
        # Since there is nothing here to delete, return None.
        #
        # IMPORTANT:
        # This does NOT mean every recursive call returns None.
        # Each call returns the root of its UPDATED subtree.
        # Here, the updated subtree is simply empty.
        if not root:
            return root

        # ---------------------------------------------------------
        # STEP 1: SEARCH FOR THE NODE
        # ---------------------------------------------------------

        # Because this is a BST:
        #
        # values smaller than root are on the LEFT
        # values larger than root are on the RIGHT

        if key > root.val:

            # The key must be somewhere in the RIGHT subtree.
            #
            # Recursively ask:
            # "Delete key from my right subtree and give me back
            #  the root of that UPDATED right subtree."
            #
            # The current function call PAUSES here while the
            # recursive call runs.
            #
            # When the recursive call returns, we reconnect the
            # returned subtree back to root.right.
            root.right = self.deleteNode(root.right, key)


        elif key < root.val:

            # Same idea, but now the key must be in the LEFT subtree.
            #
            # This current call pauses while deleteNode() works on
            # the left subtree.
            #
            # When that recursive call returns, its returned node
            # becomes our new root.left.
            root.left = self.deleteNode(root.left, key)


        else:
            # If key is neither greater nor smaller than root.val,
            # then:
            #
            # key == root.val
            #
            # We FOUND the node we want to delete.
            #
            # Now there are 3 possible deletion cases.


            # -----------------------------------------------------
            # CASE 1:
            # The node has NO LEFT child.
            # -----------------------------------------------------

            # Example:
            #
            #       10
            #         \
            #          15
            #
            # If we delete 10, then 15 should replace it.
            #
            # If this node is a leaf, root.right is also None,
            # so this correctly returns None and removes the leaf.
            if not root.left:
                return root.right


            # -----------------------------------------------------
            # CASE 2:
            # The node has NO RIGHT child.
            # -----------------------------------------------------

            # Example:
            #
            #       10
            #      /
            #     5
            #
            # If we delete 10, then 5 should replace it.
            elif not root.right:
                return root.left

            # -----------------------------------------------------
            # CASE 3:
            # The node has TWO children.
            # -----------------------------------------------------
            #
            # We cannot simply return one child because we would
            # lose the other subtree.
            #
            # Instead, replace this node's VALUE with its
            # inorder successor:
            #
            # the SMALLEST value in the RIGHT subtree.
            #
            # Why?
            # Because that value is:
            # - greater than everything in the left subtree
            # - the smallest valid value greater than root
            #
            # So the BST ordering remains valid.


            # Start at the root of the right subtree.
            cur = root.right

            # To find the smallest value in a BST,
            # keep moving LEFT as far as possible.
            while cur.left:
                cur = cur.left

            # cur is now the smallest node in the right subtree.
            #
            # Copy its value into the node we originally wanted
            # to delete.
            #
            # Example:
            #
            #       10
            #      /  \
            #     5    12
            #         /
            #        11
            #
            # Delete 10:
            #
            # smallest in right subtree = 11
            #
            # So temporarily:
            #
            #       11
            #      /  \
            #     5    12
            #         /
            #        11
            #
            # YES — at this moment there are duplicates.
            root.val = cur.val

            # -----------------------------------------------------
            # NOW DELETE THE DUPLICATE
            # -----------------------------------------------------
            #
            # We copied the successor's value into root,
            # but the original successor node still exists
            # somewhere in the RIGHT subtree.
            #
            # So now recursively delete that value from the
            # right subtree.
            #
            # Again:
            # this current call PAUSES while the recursive call runs.
            #
            # When that call returns, it gives us the UPDATED root
            # of the right subtree, which we reconnect here.
            #
            # Notice that root.val is now the successor value,
            # NOT the original key.
            root.right = self.deleteNode(root.right, root.val)

        # ---------------------------------------------------------
        # RETURN THE UPDATED SUBTREE ROOT
        # ---------------------------------------------------------
        #
        # This is the most important recursive idea in this problem:
        #
        # Every call to deleteNode() returns:
        #
        #       "the root of this subtree AFTER deletion"
        #
        # Sometimes that returned root is the same node.
        # Sometimes it is one of its children.
        # Sometimes it is None.
        #
        # Whoever called us is waiting for this returned node so it
        # can reconnect the updated subtree.
        #
        # Example:
        #
        # parent.left = deleteNode(parent.left, key)
        #
        # We return the updated subtree root →
        # parent.left receives it →
        # recursion continues unwinding up the call stack.
        return root