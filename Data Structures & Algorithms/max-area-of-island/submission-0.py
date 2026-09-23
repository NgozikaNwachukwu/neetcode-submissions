class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        maxArea = 0

        def bfs(r, c):
            nonlocal maxArea
            q = collections.deque()
            area = 1 #starting the area count at 1 becuase when bfs is called we have found a "1" which is still part of a valid area of an island and we need to account for that areas, aslo initializing it in the helper cuz i want it to reset to 1 eveytime bfs is called
            visit.add((r,c))
            q.append((r, c))
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if row in range(rows) and col in range(cols) and grid[row][col] == 1 and (row, col) not in visit:
                        q.append((row, col))
                        visit.add((row, col))
                        area += 1
                        #by the time the while loop is done we have found a valid island
            maxArea = max(area, maxArea) # should give max



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    bfs(r,c)

        return maxArea
        