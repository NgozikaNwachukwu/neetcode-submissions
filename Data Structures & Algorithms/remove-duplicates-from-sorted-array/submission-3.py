class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # the whole idea is if we find numbers that arent duplicates we put that number 
        # in l's position and increment l. so l is holding the value of unique numbers
        # if we 
        # edge case if the list is empty
        if len(nums) == 0:
            return 0
        l = 1
        for r in range(1, len(nums)): #so r is also starting at index 1
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l
        