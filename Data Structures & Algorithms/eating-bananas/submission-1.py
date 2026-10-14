class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 #ammout of banans
        right = max(piles) # amount of bananas 
        # we are doing a binary seacrh against the amount of bananas we can eat per hour to find the slowest amount of bananas we can eat per hour that wont go over the max time h
        result = right # min amount of bananas we can eat per hour for now, if we find a smaller number we can eat will replace

        while left <= right:
            mid = (left + right) // 2 # mid is the number of bananas we are testing rn for what could possibly by the min bananas we can eat
            hoursNeeded = 0
            for bananas in piles:
                hours = bananas // mid # the problem is we need to round UP due to the constrains of theproblem you must finish all bananas in a pile before moving to the next so even if our speed testing is 3, if theres a remainder of 1 banana left we have to eat that 1 banana in the one hour, we cannot take an extra 2 from another pile to make up the 3.
                if bananas % mid != 0: #if we have a remainder > 0
                    hours += 1 # we round up! cuz we need to add 1. for e.g 10/3 with the first division itll give us 3.333 whichll round down to 3, but we know we can eat 1 more since theres one left, so we add 1 to hours
                hoursNeeded += hours
            
            if hoursNeeded <= h:
                result = mid # we change our min number of bananas we can eat to satisf the probelm
                right = mid - 1
            else:
                left = mid + 1

        return result

# BINARY SEARCH EXPLANATION:
#
# left and right represent the range of possible eating speeds,
# NOT indices in the piles array.
#
# mid represents the eating speed we're currently testing.
#
# CASE 1: hoursNeeded <= h
# The current speed works because we finish within the time limit.
# We save result = mid as our smallest valid speed found so far.
# But there might be an even SMALLER valid speed!
# So we move right = mid - 1 to search the LEFT half.
# We exclude mid because we've already tested and saved it.
#
# CASE 2: hoursNeeded > h
# The current speed is TOO SLOW because we exceed the time limit.
# We need to eat FASTER, meaning we need a LARGER eating speed.
# So we move left = mid + 1 to search the RIGHT half.
# We don't update result because this speed is invalid.
#
# We stop when left > right, meaning there are no more
# possible speeds to test. Return the smallest valid speed saved.


# TIME COMPLEXITY: O(n log M)
#
# n = number of piles
# M = max(piles), the largest pile
#
# Binary search explores eating speeds between 1 and M.
# Each iteration eliminates approximately half of the possible speeds,
# so binary search takes O(log M) iterations.
#
# For EACH iteration, we loop through all n piles to calculate
# hoursNeeded, which takes O(n) time.
#
# Total: O(n) * O(log M) = O(n log M).


# SPACE COMPLEXITY: O(1)
#
# We only use a fixed number of variables:
# left, right, mid, result, hoursNeeded, hours, and bananas.
#
# We don't create any extra arrays, heaps, or data structures.
# Therefore, auxiliary space complexity is O(1).

        