class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # any connections of 1's that you can move up, left, left, right(AND NOT DIAGONALLY) isa valid island
        # so a single 1 connected by only water(all 0's surrounding it) is a valid island
        #we will have to run a BFS to be able to start from a point and search (right left up down) to find as much connecting 1's as possible. at the end of the bfs(after it finishes executing) we should have a valid island
        # now if we think about it, lets say we have an island and start at E:
        #  [ A, B, C
        #    D, E, F
        #    G, H, I]
        # to move up will be [-1, 0] -1 being the row and 0 being the column as in, the column stays the same if we are going up and down, so -1 means we are going to the row above us, so up will be B, and down will be [1, 0] so we will go to H(using the same logic) and lets say we start back at E, to go right is [0, 1] ro the row stays the same but we are moving +1, so we go to F, and left is [0, -1] as in moving backwards, so we are going to D. this is very important to understand this problem when I am revising later

        islands = 0 # initialize with 0
        rows = len(grid) # the sum of all the sub-arrays in the gris are all the rows
        cols = len(grid[0]) # the length of one row is how many colums
        visit = set() #this is to help us keep track of all the islands we have visited to make our algorithm better, so we dont visit numbers in the grid we have already visited when searching for a valid island

        def bfs(r, c):# we are searching around the number to see if it forms a valid island, AND VERY IMPORTNTLY, no co-ordinate is going to come here that is = "0" only cordinates coming here will be = "1"
            #this is a standard bfs where we are adding and popping fom the queue iteratively. but first, we need to add r and c to the que
            q = collections.deque() #create our queue
            visit.add((r, c)) #.add for sets 
            #the coordinated will be added to visited(since we are visiting (0,0) first)
            q.append((r, c)) # add the cordinates to the queue as well

            # note that if you want to add to your set 2 values instead of 1 like what we are doing you have to say, .add((a, b)) so its -> ((a,b), (c, d), (e, f)) if you dont add the values in () youll get errors. same with the queue(my fault i should know this) f youre adding values more than one, it should be .append((a,b)) so its -> [(a,b), (c, d), (e, f)] so pls be careful! this is basic python syntax pls dont make mistakes like this in the interview!

            while q: #while q has values in it
                r, c = q.popleft() # pop from queue
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]#down, up, right and left
                for dr, dc in directions: # processing by taking out each number from the subarray, e.g in the first iteration we are going down since down is the first item in the directions list, so dr will = 1 and dc = 0, this ensures that for every (r,c) (which are co-ordinated of land(1)) we search all surrounding areas to find ther land that can form an island
                    row, col = r + dr, c + dc # row and col represtns the searched co-ordinate after adding dr and dc to them

                    if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visit):
                        # first we need to check if row and col(the new co-ordintes after adding dr and dc) are valid and in range cuz if row is -1 for example thats not possible, cuz the index of rows in the grid start from 0, we cant have a -1 row.. same for colums, it just makes sure the land we are searching for is valid. SECONDLY, we  need to check if the resulting number in our new coordinates is land or water, cuz if grid[row][col] is 0 means its water, then it cannot be an island, its only valid if its = "1" and LASTLY, we check if we have already visited these co-ordines, if we have already visisted it, we cannnot add it to queue or vsit again (also cuz visist is a set and it cannot contain duplicate values), so these are the most important things to check for. An why you might ask are we adding the new co-ordines to queue if it fits all the criteria? well thats cuz we are doing a BFS! rememeber how bfs works, create a queue -> add to the queue based on some conditions(depending on the question) -> run a while loop to keep going as long as our queue has elements in it -> make a for loop to pop from our que to process the popped value(s) howeveer we eed to for the question(in this case to find out if its a valid candididate for an island search) -> add back into the queue whatever we need to whether thats the child nodes, or in this case, the new coordinates -> till we exhaust our while loop and queue has no more values in it. Therefore this is your basic BFS SEARCH! but applied in graphs :D
                        q.append((row, col))
                        visit.add((row, col)) # by the time the while loop finishes, we should have a valid island! and all the visisted spots will be stored in visisted, so that when we get to our for loop here below we will check if those co-ordinates have been visited first before re-running the bfs and incremeenting our island count, to reduce redundancy and improve our time complexity!

                    

        for r in range(rows):
            for c in range(cols):# this ensures we exhaust all columns PER ROW
                if grid[r][c] == "1" and (r,c) not in visit:# if we are on land(1) and we have not already visited this land(the position of this land) we search around it(bfs) to see if it can form a valid island!
                    bfs(r, c)
                    islands += 1

        return islands # return the number of islands at the end


        
        