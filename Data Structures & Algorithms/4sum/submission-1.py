class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 1. Sorting is mandatory so that identical values sit next to each other.
        # This allows our duplicate-skipping logic and two-pointer tracking to work.
        nums.sort()
        final = []
        
        # =====================================================================
        # LAYER 1: The Outermost Loop 'i' -> O(n) steps
        # =====================================================================
        for i in range(len(nums)):
            # Skip duplicates for the 1st number:
            # If we already processed this exact number in the previous turn,
            # skip it to prevent duplicate quadruplet combinations.
            if i > 0 and nums[i-1] == nums[i]:
                continue
                
            # =====================================================================
            # LAYER 2: The Second Nested Loop 'j' -> O(n) steps
            # =====================================================================
            # This loop spins fully from left to right for EVERY single step 'i' takes.
            for j in range(i + 1, len(nums)):
                # Skip duplicates for the 2nd number:
                # 'j > i + 1' ensures that on its very first turn, 'j' is allowed
                # to be identical to 'i' (e.g., [2, 2]). But on any subsequent turns,
                # if 'j' lands on a duplicate value, it skips ahead.
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                
                # =====================================================================
                # LAYER 3: The Pointer Hunt 'while l < r' -> O(n) steps
                # =====================================================================
                # For every fixed pair of (i, j), these two pointers scan the remaining
                # elements on the right. This third layer multiplies the complexity to O(n³).
                l = j + 1
                r = len(nums) - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total == target:
                        # Valid quadruplet found! Add it to our results list.
                        final.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        # Move both pointers inward to look for other pairs
                        l += 1
                        r -= 1
                        
                        # Skip duplicates for the 3rd number (left pointer):
                        # Keep pushing 'l' right if it lands on the same value it just used.
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        # Skip duplicates for the 4th number (right pointer):
                        # Keep pushing 'r' left if it lands on the same value it just used.
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                            
                    elif total < target:
                        # If the total is too small, move 'l' right to get a larger value
                        l += 1
                    else:
                        # If the total is too large, move 'r' left to get a smaller value
                        r -= 1  
                        
        return final


                        
        