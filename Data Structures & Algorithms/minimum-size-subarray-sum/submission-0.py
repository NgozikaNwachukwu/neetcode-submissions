class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 #starting at the beginning
        total = 0 #we will be keeping a running total
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                #shrink from the left side
                #as we are shrinking we have to subtract the number at l
                #from our window since itll no longer exist
                #as long as our window is valid
                total -= nums[l]
                l += 1
        if res == float('inf'):
            return 0
        else:
            return res