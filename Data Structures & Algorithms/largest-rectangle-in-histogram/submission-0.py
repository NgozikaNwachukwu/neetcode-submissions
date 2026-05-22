class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #basically in a histogram(each element in the array being the height of each rectangle)
        #we need a stack to be able to look back at the previous height
        # this stack will holf (index, height) pair
        # the whole point is the histogram should be in increasing order
        # if a smaller rectangle comes after a taller rectangle its no longer in ascending order
        # when that happens we need to pop out the prevoius taller rectangle
        # then after we pop it out we calculate its area
        # and we are going to have a variable maxArea that keeps track of the maxArea
        # and its the max area that we will return
        # after tracking the maxArea, we need to kind of extend the smaller rectangles area
        # we do this by setting the start idex to the index of the rectange we just popped out
        #so thats kind of extending its width(cuz since its smaller it can extend through the previous taller rectangle)
        #the longer rectangle couldnt extend forward because the next rectangle was shorter, so there was a gap
        # but if the next rectange is bigger(ascending order) then we dont need to pop
        # any way after we pop, there will be rectangles in the stack
        # we need to cross check the remaining rectangle blocks by calculating their area
        # and then comparing with the max area, incase the maxarea is with theese rectangles that were not popped
        # we do this by multiplying the height by the whole length of the array - its index instead, why? im guessing:
        # the remaining rectagle(s) might either be alone or spaced out, they have nothing else to
        # calculate their area by. by the way, area of a rectangle is height x width
        # this is the best way i have understood this problem

        stack = [] # in index-height pairs so e.g [(1,2), (2,4)]
        maxArea = 0 # initializing it to 0
        
        for i, h in enumerate(heights):
            start = i # this is what enables us to extend the width backwards
            #if we are not in ascending order. so we can tack wher the width starts from
            while stack and h < stack[-1][1]: # meand the height in the topmost element
            # the satck is in index-height pairs. meaning if we follow the example above, 
            # (2, 4) is the topmost element so since index-height, stack[-1][1] will be 4!
                index, height = stack.pop() # this pops the index and height so 2 and 4 (following above example)
                area = height * (i - index) # we will be at the next index if we are looking into a past taller rectangle
                # so to get the area of ONLY that popped rectangle, we need to subtract the current index we are on by the index
                # of our popped rectangle :)
                maxArea = max(maxArea, area)
                start = index # what i said about extending the width of the currecnt rectangle we are on backwards
                # because since its smaller it can extend towards the previous rectangle(cut through)
            stack.append((start, h))

        # now we need to calculate the heights of the remaining rectangles in the stack
        # we do this cross check incase the maxArea in gotten from one of thse rectangles
        # we will be subtracting the length of the histogram from the index of the remaining rectangle(s)
        # because there is nothing else to subract it/them by (i think this is the reason)
        for i, h in stack:
            leftover_area = h * (len(heights) - i)
            maxArea = max(maxArea, leftover_area)
        
        return maxArea

        