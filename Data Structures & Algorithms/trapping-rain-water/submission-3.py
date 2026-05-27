class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: # edge case for if the list is empty
            return 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        result = 0
        # the aim of this is, we want to calculate the amount of water stored at each
        # index(on top of each wall)
        # to be able to find the amount of water on top of each wall, we need to find the maximum left height(wall height)
        # and we need to find the maximum right height
        # the we subtract those from the current wall we are on
        # if this was a O(n) space, we can use 3 lists
        # we can iterate through the list left to right to find out the highest left wall at each point(left to the current wall we are on)
        # then store that in one list(preferably a stack)
        # then iterate through the list backwards to find the highest wall to the right of each wall
        # then store in the next stack. in a third list you can pop each of the other stacks and compare what the lowest value is
        # then subtract each lowest value in the third list from each of the walls in the original list
        # then add all of it together
        # however, since we are using 2 pointers, we are going to update the leftMax by the maximum value of the current wall and and the current leftmax value
        # we will subtract the leftMax value with the height of the current wall we are on to find out the amount of water stored on top of that current wall
        # then add that to res
        #we will move a pointer forward depending on the lefmax and right max values
        # if the leftmax is less than or = to right max we will be moving l forward and doing the check
        # if rightmax is less, we will be moving r forward, checking to see if the height of the current wall is greater than rightmax and update rightmax to the taller value
        # then add the rightmax minus the height of the current wall to res
        #that is our algorithms
        #writing this out for study purposes
        while l < r:
            if leftMax <= rightMax: # move l as long as leftmax is less then rightmax or equal to rightmax. we can move either if they are equal! i am choosing to always move l when they are equal
                l += 1
                leftMax = max(height[l], leftMax)
                result += leftMax - height[l] # to find out how much water is stored on top of this wall
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                result += rightMax - height[r]
        return result
                
        
        