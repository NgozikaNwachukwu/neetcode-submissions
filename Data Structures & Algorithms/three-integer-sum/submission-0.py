class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # create the final array
        # It puts identical numbers next to each other so we can easily skip duplicates.
        nums.sort() # sort the list

        for i, num in enumerate(nums):
            # 2. Early Break Optimization:
            # Since the list is sorted, if our fixed first number (num) is greater than 0,
            # all numbers after it are also positive. It is impossible for three 
            # positive numbers to add up to 0, so we terminate the entire loop early.
            if num > 0:
                break
            # 3. Skip Duplicates for the First Number:
            # If this is not the first element (i > 0) and it matches the value at the 
            # previous index (nums[i-1]), skip it using 'continue'. This prevents us 
            # from generating duplicate triplet combinations.
            if i > 0 and num == nums[i-1]:
                continue

            # 4. Initialize Two Pointers:
            # 'l' (left pointer) starts right after our fixed first number.
            # 'r' (right pointer) starts at the very end of the array.
            l = i + 1
            r = len(nums) - 1
            # 5. Two-Pointer Window Search:
            # Shrink the window from both sides to find pairs that match our fixed 'num'.
            while l < r:
                # Calculate the sum of the current three numbers
                threeSum = num +nums[l] + nums[r]
                if threeSum > 0:
                    # If the sum is too large, move the right pointer inward 
                    # to make the next sum smaller (since the array is sorted).
                    r -= 1
                elif threeSum < 0:
                    # If the sum is too small, move the left pointer inward
                    # to make the next sum larger.
                    l += 1
                else:
                    # 6. Valid Triplet Found:
                    # Save the combination to our results list.
                    res.append([num, nums[l], nums[r]])
                     # Move both pointers inward to look for other potential pairs
                    # that could work with the current fixed 'num'.
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                    # 7. Skip Duplicates for the Second Number:
                    # After shifting 'l', check if the new element is identical to the 
                    # one we just used (nums[l-1]). If it is, keep moving 'l' forward
                    # until we hit a brand-new number. This avoids duplicate triplets.
                        l += 1
        return res # return the list

        

        