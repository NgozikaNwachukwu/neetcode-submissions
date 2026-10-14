class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #we are pretending like this is a 1D array and making formulas to traverse grapgh as if it was a 1d array. row = mid//m and col = mid%m where m is number of columns 
        #this is how we can traverse the graph with a binary search algorithm
        n = len(matrix) #rows
        m = len(matrix[0]) # colums

        left = 0 # starts at the beginning
        right = (n * m) -1 #starts at the end
        
        while left <= right:
            mid = (left + right) // 2 # mid
            row = mid // m
            col = mid % m

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1 # move left forward if less
            else:
                right = mid - 1 # move right to right before mid if number is >

        return False

        