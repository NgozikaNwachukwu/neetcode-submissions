class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 # at the start
        right = len(nums) - 1 #at the end

        while left <= right:
            mid = (left + right) // 2 #mid will be re-calculated each loop
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # if mid is less than target it means that our target is to the left(since our array is gauranteed to be sorted)
                left = mid + 1 # move left ahead of current mid
            else:
                right = mid - 1 # move right ahead oh mid(the other direction)

        return -1#target doesnt exist in nums array
        