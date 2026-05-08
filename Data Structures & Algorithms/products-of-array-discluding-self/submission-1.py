class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize output array with 1s.
        # If nums = [1, 2, 4, 6], n = 4.
        output = [1] * n #e.g length of nums array is 4, output is: [1,1,1,1]

        #using the prefix - suffix pattern
        # --- PHASE 1: FORWARD PASS (Prefix) ---
        # Goal: Each index i will store the product of all elements to its LEFT.
        prefix = 1
        # range(n) goes 0, 1, 2, 3. It stops BEFORE index 4.
        for i in range(n):
            output[i] = prefix  # Put the current running product into the slot.
            prefix *= nums[i]   # Update the product for the NEXT index to use.

        # Trace for nums = [1, 2, 4, 6]:
        # i=0: output[0]=1, prefix becomes 1*1 = 1
        # i=1: output[1]=1, prefix becomes 1*2 = 2
        # i=2: output[2]=2, prefix becomes 2*4 = 8
        # i=3: output[3]=8, prefix becomes 8*6 = 48
    
        # After this loop, output is [1, 1, 2, 8]

        # --- PHASE 2: BACKWARD PASS (Suffix) ---
        # Goal: Multiply what's already in output[i] by the product of all elements to its RIGHT.

        suffix = 1
        # range(n-1, -1, -1) starts at index 3, stops BEFORE -1 (at index 0).
        for j in range(n-1, -1, -1):
            output[j] *= suffix  # Multiply the existing Left-product by the new Right-product.
            suffix *= nums[j]    # Update the product for the NEXT index (moving left).

        # Trace for nums = [1, 2, 4, 6]:
        # i=3: output[3] = 8 * 1  = 8,   suffix becomes 1*6 = 6
        # i=2: output[2] = 2 * 6  = 12,  suffix becomes 6*4 = 24
        # i=1: output[1] = 1 * 24 = 24,  suffix becomes 24*2 = 48
        # i=0: output[0] = 1 * 48 = 48,  suffix becomes 48*1 = 48

        return output

        