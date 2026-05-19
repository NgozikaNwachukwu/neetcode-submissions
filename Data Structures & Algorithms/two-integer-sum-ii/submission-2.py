class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since the list is sorted
        l = 0 #pointer at the beggining
        r = len(numbers) -1 # pointer at the end
        
        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target: # if the sum is greater than target that means we 
        #need to move r backwards(the list is sorted) so moving r bacward, the
        #number is reducing and helps us get closer to target
                r -= 1
            elif currSum < target: 
                l += 1 # we are moving the l pointer forward cuz since its sorted as we 
            #are moving forward the numbers increase(whch helps us get closer to target)
            else:
                return [l+1, r+1]
        
        return []