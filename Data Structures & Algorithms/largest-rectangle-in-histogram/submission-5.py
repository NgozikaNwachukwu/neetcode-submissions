class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                area1 = height * (i - index)
                maxArea = max(maxArea, area1)
                start = index
            stack.append((start, h)) #take the width to the start of the rectangle you just popped! (take it back cuz u can)
                
            

        for i, h in stack:
            area2 = h * (len(heights) - i)
            maxArea = max(maxArea, area2)
        
        return maxArea

        