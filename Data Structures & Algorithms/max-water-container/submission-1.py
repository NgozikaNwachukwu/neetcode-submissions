class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = height * width
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

        # this is the O(n) time solution! the previous was O(n^2) both are of 
        #space O(1)



        