class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        final = []
        l = 0
        r = k-1
        if len(nums) == 0:
            return []
        while r < len(nums):
            subArr = nums[l:r+1]
            highest = max(subArr)
            final.append(highest)
            l += 1
            r += 1
        return final

        #my brute force(that actually worked on first try lmao)

        