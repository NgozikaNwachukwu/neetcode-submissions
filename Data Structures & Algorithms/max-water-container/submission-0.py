class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            l = i
            r = l + 1
            while r != len(heights):
                width = r - l
                if heights[r] == heights[l] or heights[r] < heights[l]:
                    area = width * (heights[r])
                else:
                    area =  width * (heights[l])
                maxArea = max(maxArea, area)
                r += 1
        return maxArea



        