# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #basic BFS!

        results = []
        queue = collections.deque()
        current_node = root
        queue.append(current_node)
        #start with adding the root to the queue so we dont have an empty queue, unless thw hile loop will never run

        while len(queue) > 0:
            #we need to add nodes into the queue and we will add the value of the nodes into the result

            qLen = len(queue) #this ensures we go through the tree one level at a time
            level = [] # for each level we will ad it to its own list(which is called level), and for every level list, we will append it to the results array
            for i in range(qLen):
                current_node = queue.popleft() #pop from the left
                if current_node:
                    level.append(current_node.val)
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            if level: # our queue can have null nodes so we have to check if the level list has values in ot before appending to results list. For instance, if we get to the point our queue has all null nodes, the "if current_node:" line wont run cuz its false, the currently popped node is null, so the level list is still empty(from the initialization in the while loop that resets the list back to empty when its time for a new level)
                results.append(level)

        return results
            


        