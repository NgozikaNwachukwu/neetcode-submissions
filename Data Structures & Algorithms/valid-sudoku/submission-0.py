class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #validate the rows
        for i in range(9): #we are checking each row since a row has 9 boxes
            s = set() #create a new set that will check each row
            for j in range(9): #j represents columns
                item = board[i][j] # e.g item at row 1, column 1(thats how we check)
                if item in s: # if the item is in the set theres a duplicate
                    return False
                elif item != '.': # if item isnt '.' because we dont want to interact with the full stops
                    s.add(item)


        #validate the columns(similar)
        for i in range(9):
            s = set() # make a brand new set for each column
            for j in range(9):
                item = board[j][i] # now we are checking colums, e.g number in col 1, row 1
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)



        #validate the 3x3 boxes
        #have a nested for loop for each of the positions
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)] # these are all the start positions
        for i, j in starts:
            s = set() # make a new set after each box
            for row in range(i, i+3): # stops at i+2 since stop is exclusive, rows of the box
                for col in range(j, j+3): # columns of the box
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True

        