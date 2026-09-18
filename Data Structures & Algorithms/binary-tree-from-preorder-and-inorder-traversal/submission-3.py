# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder of a tree always starts at the root then goes left
        #inorder of a tree goes as left as possible before processing nodes, meaning, the first few nodes in the array represent the left tree right before the node.
        #how we will construct the tree is simple, we will know that the root is the first number in preorder, then if we find the root in the inorder, we basically will find out how many nodes are in the left subtree and know that all the nodes to the right of the root are in the right subtree and this will allow is to know the subarray in th preorder list that represents the nodes in the right subtree. and next now that we know the left subtree comes before the root in inorder and for post order its root>left subtree> right subtree we know exactly how many nodes are in the left tree, so right after the left subtree ends we know in the preorder list the immediate next node is the root of the RIGHT subtree. because yes inorder lets us know the number of nodes in the right subtree it doesnt tell us the root of the right subtree, now we know that amount, we know the root(of the right subtree) from the preorder array. now we can locate the root in the inorder array, and know that anything to the right of the root(of the right subtree) is its left subtree and anything to the right is its right subtree for sure. we could kind of decipher that from the preorder, but the inorder lets us know the exact amount of nodes to the left of the root of the rightsubtree and the amount of nodes in the right subtree as well. 
        #basically we need to manipulate the arrays by first creating the root then finding the index of the root in the inorder array and then recursively build the left subtree by starting from index 1(root of the left subtree)(in preorder array) till mid+1 cuz mid (the index of root in inorder array) is the exact number of nodes in the left subtree and how range works if we do 1 - mid then itll stop at mid -1(not include all th nodes in left tree) and then the inorder array will be from the beginning of the array till mid(cuz we dont want to incluse the root of the entire tree) also cuz from the begining till mid represents all the nodes in the left subtree in the inorder array

        #start wth base case which is usually if its empty return None
        #if not preorder or not inorder:
        #    return None

        #root = TreeNode(preorder[0]) # create the root since root is first val in preorder
        #mid = inorder.index(preorder[0]) #the index of the root in inorder array

        #root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        #root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        #return root

        #too slow O(n^2)

        preIdx = inIdx = 0
        def dfs(limit):
            nonlocal preIdx, inIdx
            if preIdx >= len(preorder):
                return None
            if inorder[inIdx] == limit:
                inIdx += 1
                return None

            root = TreeNode(preorder[preIdx])
            preIdx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))

        