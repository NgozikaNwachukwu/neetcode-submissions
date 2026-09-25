"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        #the algorithm for this is, we need to first clone each node and store the clone of that node in a dictionary mapped to itseflf as in Node : "clone" (key : "value") and then as we are going, we are also cloning the neghbours of every node, recursively. so if we try to clone a neighbour, and we recursively try to clone its neighbours, but it has already ben stored in the dictionary, then we return  the clone we already made
        clones = {} # the dictionary where we map node -> its clone
        def dfs(node):
            if not node: # base case
                return None
        
            if node in clones:
                return clones[node] # base case

            copy = Node(node.val) # make a new node and give it the value of the current node
            clones[node] = copy # map the node to its copy
            for neib in node.neighbors: # neighbours is a list as shown above
                copiedNeib = dfs(neib) # run the function recursively on neighbor and store in this variable
                copy.neighbors.append(copiedNeib) # we are making clones of the copied nodes neighbour as well! not just cloning the node but its neibours as well, thats the process of connecting the edges together
            return copy
#`copy` represents the copied version of the CURRENT node for THIS specific
# dfs(node) call. Every recursive dfs call has its own local `copy`.
#
# For example:
# dfs(Node1) creates CopyNode1
#   -> dfs(Node2) creates CopyNode2
#       -> when dfs(Node2) finishes, `return copy` returns CopyNode2
#          back to the paused dfs(Node1) call.
#
# This is important for:
# copy.neighbors.append(dfs(nei))
#
# dfs(nei) returns the COPY of that neighbor, so we are essentially doing:
# CopyNode1.neighbors.append(CopyNode2)
# This connects COPIED nodes to other COPIED nodes.
#
# Eventually, the ORIGINAL dfs(starting_node) call finishes and `return copy`
# returns the copied version of the starting node (e.g. CopyNode1).
# That copied starting node gives us access to the ENTIRE cloned graph because
# its .neighbors point to copied neighbors, whose .neighbors point to more
# copied nodes, etc.
#
# Similar to returning the root of a tree: we don't return every node separately.
# We return the starting/root node, and its connections give access to the
# entire structure.

        return dfs(node)





        