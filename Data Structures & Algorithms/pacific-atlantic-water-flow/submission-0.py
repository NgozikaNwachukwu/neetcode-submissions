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


        