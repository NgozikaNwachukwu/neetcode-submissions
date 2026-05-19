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
        while i <= r: # because we need to check the number at i
            if nums[i] == 0:
                swap(i, l)
                l += 1 # move l forward
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1 # to ensure i doesnt move forward if we find that i is 2
            i += 1

        
            

        