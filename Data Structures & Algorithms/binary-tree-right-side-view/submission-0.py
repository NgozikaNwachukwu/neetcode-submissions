# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we will use breath-first search to solve this
        #which is level order traversal

        #first we will need to add the root to the queue(like bfs starts)
        #then start our while loop while queue hav elements in it
        #the trick is, since bfs enables us to go level by level anyways
        #we manipulate WHEN we add a nodes value to the final results list
        # because since the problem only wants right facing nodes
        #we can loop through each level and only ad the LAST node for that
        #particular level. That node we will be adding will be the right
        #side view node. and if that node is the only node in its level,
        #whether that be a left child node or right child node,
        #as long as its the only node it can still be seen from the right
        #side, and is technically, the last and only node we will add
        #for tht level. so the algorithm works perfectly 
        #whether there are 4 nodes in one level or 1 node for that level
        #this algorithm will only return the nodes from the right-view
        #by returning the very last nodes(from the right) for that level
        #by manipulating WHEN we will be adding it to the final results
        #list. which is AFTER the loop has finished(cuz itll be on the final node for that level by the time is done, therefore adding the last node for that level!)

        results = []
        q = collections.deque()
        q.append(root) # add root first

        while len(q) > 0:
            qLen = len(q) #keeping track of the length for the for loop
            rightMost = None # initializing rightmost node

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left) #important that you add left first
                    q.append(node.right)

            #now after the loop finishes:
            if rightMost:
                results.append(rightMost.val)

        return results
        


        