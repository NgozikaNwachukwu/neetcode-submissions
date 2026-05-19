class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def swap(i, r):
            temp = nums[i] # temporary location to store the number at this pointer(index)
            nums[i] = nums[r] # replace what is currently in nums[i] with whats in nums[r]
            #this is okay because we saved a copy of whats in nums[i]
            nums[r] = temp # now putting the copy of what was in nums[i] and replacing it with nums[r]

        i = 0 #scout
        l = 0
        r = len(nums) -1
        # === 1. WHY THE BOUNDARY IS i <= r ===
        # 'r' marks the boundary where unexamined numbers end and sorted 2s begin.
        # When 'i' equals 'r', index 'i' is standing on a number that was swapped 
        # there from the back, meaning it has NEVER been checked yet. 
        # If we used '<', we would stop early and leave this last number unexamined.
        while i <= r: # because we need to check the number at i
            if nums[i] == 0:
                swap(i, l)
                l += 1 # move l forward
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                #=== 2. WHY WE DECREMENT i HERE ===
                # When we swap with 'r', we pull an UNKNOWN number from the back to index 'i'.
                # That new number could be a 0, 1, or 2. We cannot move 'i' forward yet 
                # because we must inspect this new number first.
                #
                # By doing 'i -= 1' right before the loop naturally does 'i += 1' at the bottom,
                # the two operations cancel each other out (i - 1 + 1 = i). 
                # This effectively FREEZES 'i' in place for the next loop iteration.
                i -= 1 
            # This moves 'i' forward to the next number. 
            # (If the 'elif' block ran, this just brings 'i' back to its current position).    
            i += 1

        
            

        