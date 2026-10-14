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


        