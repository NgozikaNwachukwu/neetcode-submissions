class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(set(nums)) #sorting and removing duplicates
        longest = 1 
        current = 1 #these are both counting the sequence

        for i in range(len(nums)):
            if nums[i] - nums[i-1] == 1: 
                current += 1
                if current > longest:
                    longest = current
            else:
                current = 1 #resets the sequence count
        return longest
