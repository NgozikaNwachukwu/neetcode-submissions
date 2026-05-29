class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # so we reverse the whole list
        # the reverse the first k elements
        # then reverse the remaining elements in the list

        k = k % len(nums) # we are modding k by the length
        # the reason we do this is to handle the case whereby k > len(nums)
        # which was an error i had with testing
        l = 0
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
         # apparently you can do this in place without a temporary variable
            l += 1
            r -= 1
        #now we have successfully reversed the list

        l = 0 
        r = k - 1# reversing the first k elements. k-1 stops at the kth number
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] # apparently you can do this in place without a temporary variable
            l += 1
            r -= 1

        l = k # cuz we want to start at the number after the kth number
        # to ensure that we are reversing the rest of the list
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l] # apparently you can do this in place without a temporary variable
            l += 1
            r -= 1
