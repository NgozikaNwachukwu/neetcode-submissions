class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #basically we are checking if cell can flow to the atlantic and pacific
        #we make 2 visisted sets pacific and atlantic
        #2 queues atlanticq and pacificq
        #and what the bfs is doing is looking for the neighbours of all the "boardering cells"
        # meaning all the cells at the bottom and right are flowing into the atlantic and all the cells at the top and left are flowing into the pacific
        # we ad all those cells to the sets and queues first, then in the actual bfs, and what the bfs is doing is looking for all the neighbours of those cells that can flow into the "boardering cells" that will allow the water to flow into the ocean. so if a cell is >= to a boadering cell, then water can flow DOWN into that ocean from the boardering cell. 
        #so bfs is basically looking for all the neighbours of the boardering cell and the neighbours of those neighbours(that aent in the visited set of course)
        #the bfs is only SEARCHING, its not actually checking to see if a cell flows into both
        # so after we call bfs on the pacific side(pacific queue and pacific set) and atlantic side(atlantic queue and atlantic set) we check for those cells that are both in atlantic set and the pacific set. if a particular cell exists in both those sets it means water can flow into both oceans from that cell!(the intersection)
        #then we add that to the list

        rows = len(heights)
        cols = len(heights[0])

        pacific = set()
        atlantic = set()

        atlanticq = collections.deque()
        pacificq = collections.deque()

        directions = [[1,0], [-1,0], [0,1], [0,-1]] #down, up, right, left

        #bfs starts here:
        def bfs(q, visited):
            while q:
                r, c = q.popleft() # pop coordinates values out of queue
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc # searching
                    if row in range(rows) and col in range(cols) and (row, col) not in visited and heights[row][col] >= heights[r][c]:
                        #if row and col in range, have not been visited and larger than the currect heights[r][c]
                        q.append((row, col))
                        visited.add((row, col))

        #collecting topmost cells(boardering the pacific) and bottom-most cells(boardering the atlantic)
        for c in range(cols):
            pacific.add((0, c))
            pacificq.append((0, c))

            atlantic.add((rows - 1, c))
            atlanticq.append((rows - 1, c))
        #collecting leftmost cells(boardering the pacific) and rightmost cells(boardering the atlantic)
        for r in range(rows):
            pacific.add((r, 0))
            pacificq.append((r, 0))

            atlantic.add((r, cols - 1))
            atlanticq.append((r, cols - 1))

        bfs(pacificq, pacific)
        bfs(atlanticq, atlantic)

        results = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r,c) in atlantic:
                    results.append([r, c])

        return results



#for future reading:

# TIME COMPLEXITY: O(R * C)
# R = number of rows, C = number of columns.
# N = R * C = total number of cells in the grid.
#
# 1. The first two for loops collect the ocean border cells.
#    The column loop takes O(C), and the row loop takes O(R).
#    Together, that's O(R + C).
#
# 2. We run BFS twice: once for Pacific and once for Atlantic.
#    In each BFS, a cell is added to the visited set as soon
#    as it is added to the queue.
#    This prevents that cell from being added again through
#    another path, even if multiple neighbors can reach it.
#    (The starting corners may be queued twice, but this is
#    only a constant number of extra operations.)
#
#    Therefore, across ONE ENTIRE BFS, each cell is processed
#    at most once, apart from those constant duplicates.
#    Since there are R * C cells, BFS processes O(R * C) cells.
#
#    For EACH popped cell, we check exactly 4 directions.
#    So one BFS takes O(4 * R * C) = O(R * C).
#
#    Two BFS calls: O(R * C) + O(R * C) = O(2RC).
#
# 3. The final nested for loop checks every cell to see if
#    its coordinates exist in BOTH visited sets.
#    Set membership checks are O(1) on average.
#    Therefore, this loop takes O(R * C).
#
# TOTAL TIME:
# O(R + C) + O(2RC) + O(RC)
# = O(R + C + 3RC)
# = O(R * C), since RC dominates and constants are dropped.


# SPACE COMPLEXITY: O(R * C)
#
# 1. We create TWO visited sets: pacific and atlantic.
#    In the worst case, every cell can reach both oceans.
#    Each set could contain R * C coordinates.
#    Together: O(2RC) = O(R * C).
#
# 2. We create TWO BFS queues.
#    A queue stores coordinates waiting to be explored.
#    In the worst case, a queue can hold O(R * C) cells.
#    Together, both queues require at most O(R * C) space.
#
# 3. The results list can contain every cell's coordinates
#    if all cells can reach both oceans.
#    Therefore, the output can use O(R * C) space.
#
# 4. Variables like rows, cols, r, c, row, col, dr, dc,
#    and the four-element directions array use O(1) space.
#
# TOTAL SPACE:
# O(R * C) for visited sets + O(R * C) for queues
# + O(R * C) for results + O(1) for other variables
# = O(R * C).
#
# Even if we exclude the output list from auxiliary space,
# the visited sets and queues still require O(R * C).



        