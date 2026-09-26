class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #so miniute by minute is basically a level and a level is all the moves that can be taken by the starting rotted fruit(s) aka the moves that can be taken by the rotten fruit(s) that are currently inthe queue), starting from the rotten fruit(s). if we go through a level and find any fresh fruit, thats a single minute! and once thats popped out of the queue, we add the newly rotted fruits. we will be BFS for this. since we need the level by level breakdown to count each minute! THERE CAN BE MORE THAN ONE ROTTEN FRUIT AT THE START(more than one "2")

        visit = set()
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        fresh = 0 #number of fresh fruits
        
        def bfs():
            nonlocal minutes
            nonlocal fresh
            while q and fresh > 0: # stops if one becomes false(TRUE&FALSE = FALSE) also just so when i come back in the future to read this problem is, the reason we add fresh > 0 to the while loop is to handle the edge case of what if there are unexplored levels, like levels remaining, but there are NO fresh fruit left to rot? cuz a minute can only be counted if a ROTTEN fruit is rotting a frh fruit(aka it is within direction of a fresh fruit(s) to rot them) so what if there are levels left in the grid that we havent explored, but theres no fresh fruit left to rot? (this isnt always the case, sometimes the case can be we have explored all levels and the queue is officially empty but there are fresh fruit still left that we werent able to rot/reach with the directions constraints, in that case we return -1 as handles below) so this is to handle the case that theres no more fresh fruit to rot, that way if we reach other level the while loop will fail cuz TRUE AND FALSE = FALSE. so we dont give unneccesary extra minutes for levels for NO MORE fresh fruits. WE ONLY COUNT OF A LEVEL IS ROTTING FRESH FRUIT! IF A LEVEL ISNT ROTTING AN FRESH FRUIT WHETHER THAT BE BECAUSE WE CANNOT REACH IT OR BECAUSE THERES NO MORE FRESH FRUIT LEFT TO ROT, WE DONNOT COUNT THAT LEVEL!
                qLen = len(q)
                for _ in range(qLen): # per level pop(meaning we will pop all the rotted fruits for a level, and a level is all the moves that can be taken by the starting rotted fruit(s) aka the moves that can be taken by the rotten fruit(s) that are currently inthe queue)
                    r, c = q.popleft()

                    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        row = r + dr
                        col = c + dc
                        if row in range(rows) and col in range(cols) and grid[row][col] != 0 and (row, col) not in visit:
                            q.append((row, col))
                            visit.add((row, col))
                            fresh -= 1 # decrement fresh
                    
                        #at the end of this newly rotted fruit(formally fresh fruit) will be added to the queue
                minutes += 1 # minutes are only incremented after each level search
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c)) # adding the rotten fruit2 to the queue and the visit set to mark that we have visited it before the bfs!
                elif grid[r][c] == 1:
                    fresh += 1

        bfs()

        if fresh > 0: #there are fresh fruits left that we couldnt reach with our directional constraints after exploring every level!
            return -1
        return minutes # return minutes at the end
                    

     # Time: O(N), where N is the total number of cells in the grid.
# We initially scan every cell once. During BFS, each reachable fruit
# is added to the queue at most once, and we check 4 directions for
# each fruit. Therefore O(N) + O(4N) = O(N).

# Space: O(N).
# In the worst case, the visited set and BFS queue can contain
# O(N) cell coordinates.

#Or, if they want rows/columns explicitly:

#Time: O(R × C) and Space: O(R × C)  