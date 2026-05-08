class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums): # this ensure that each number in the array had a index
            #calculation : num1 + num2 = target
            #if we carry over num1 = target - num2
            #num1 becomes our complement
            complement = target - num
            if complement in my_dict:
                return [my_dict[complement], i]
                #what this does is return the idex of i's complemnt and i, in an array
            
            else:
                my_dict[num] = i # we are setting the value of complent to be the index of the current number
        return [] # this handles if none of the numbers add up to target or for an empty list

        #test cases:
        #[3,4,5,6] t = 7
        #3: 0
        #4: 1
        

    
        