class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        # Our window currently covers the entire array.

        # We need to shrink this window until exactly 'k' elements remain.
        # 'r - l' calculates how many spaces are between our pointers.
        # As long as that gap is greater than or equal to k, we have too many
        # elements and must eliminate the worst option.
        while r - l >= k:
            # abs(x - arr[l]) calculates the distance from target x to the left number.
            # abs(x - arr[r]) calculates the distance from target x to the right number.
            #
            # The `<=` handles the tie-breaker rule perfectly:
            # - If the left number is closer, it stays, and we eliminate the right (r -= 1).
            # - If it's a perfect tie, the problem prefers the smaller left number.
            #   So the left number still wins, and we eliminate the right (r -= 1).
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1  # Right number is further away (or tied), throw it away!
            else:
                l += 1  # Left number is further away, throw it away!

        # Once the loop ends, 'l' and 'r' perfectly frame our k closest elements.
        # Python slicing [start:end] is EXCLUSIVE of the 'end' index.
        # We use 'r + 1' so that the element sitting at index 'r' is included.
        return arr[l: r + 1]


        # =============================================================================
# COMPLEXITY ANALYSIS (WRITTEN WITHIN THE CODE)
# =============================================================================
# Let N = total number of elements in the array.
# Let K = the number of closest elements we need to return.
#
# TIME COMPLEXITY: O(N - K)
# Why? We start with a total pool of N elements. Every single turn of the loop,
# we eliminate exactly 1 element. We stop looping the moment we have K elements left.
# Therefore, the loop must run exactly (N - K) times to throw away the losers.
# Inside the loop, we only do basic math comparisons, which take O(1) constant time.
# Total Time = (Number of loop turns) * O(1) = O(N - K).
#
# SPACE COMPLEXITY: O(1) Auxiliary Space
# Why? The algorithm only creates two integer pointers (l and r) and a few math
# variables to track distances. It does not use any extra arrays, maps, or hashes
# that scale up with the input size.
# Note: If your interviewer asks you to count the mandatory output list returned
# at the end, that list takes up O(K) space because it holds K elements.
        