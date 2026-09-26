class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        #the algorithm is using BFS, to search for infinities(land), instead of searching for treasures(0) from land. And we cannot traverse through water. BFS effectively helps us find the distance from each land to a treasure chest, and gives the lowest distance possible. We will first, search for treasure(0's) and store it in the queue. the bfs will basically be us popping the 0's from the queue, and seaching for land with directions(left, right, down, up) and and if that part of the graph is vald and in range, itll change to 0+1, and when traversed again, we will keep adding 1. amd both 0's will spread out at the same time as we are traversing(since we are adding both to the queue)

        q = collections.deque()
        visit = set()

        rows = len(grid)
        cols = len(grid[0])

        # Find ALL treasures first
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))  # treasure is already discovered

        def bfs():
            while q:
                r, c = q.popleft()

                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1]
                ]

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (
                        row in range(rows)
                        and col in range(cols)
                        and grid[row][col] != -1
                        and (row, col) not in visit
                    ):
                        # Distance = current cell's distance + 1
                        grid[row][col] = grid[r][c] + 1

                        # Mark it visited AS SOON as we add it to queue
                        visit.add((row, col))
                        q.append((row, col))

        bfs()