class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # the whole idea in this prefix sum appraoch
        # is that there is a current sum, which is the sum of the numbers
        # as we are interating through the array
        #the current sum + past sum(which is the sum we just passed) = k
        # so current sum - k = past sum
        # if you think about it, between the past sum, and current sum
        # its k between them. so that shows that there are valid subarrays
        #between the past sum and our current sum! :)
        # a dictionary is going to help us keep track of our past sums
        # so that if we do find a past sum, its valu is the amount of subarrays that can be formed
        # since negative numbers are allowed in the array, a past sum can have
        # a value great than 1
        # so we are basically looking into the past and asking, is ther a past sum
        # that between that past sum and this current sum is equal to k?
        # because if there is a past sume, the amunt of times we've seen that past sum
        # is the amount of times we can form valid sub arrays!
        # a very important edge case is if the first number in the array is = k
        # for example nums: [3,4,2,1] k = 3. [3] is a valid subarray, as in
        # the first number alone can form a valid subarry since k is 3 
        # and subarray sums up to k. but if we use our logic
        # the current sume will be 3, 3-3 = 0, and no 0 exists in our dictionary yet
        # because initially our dictionary is empty, so the result will not be incremented!
        # and if we dont increment that first number, our final number of subarrays formed will be wrong
        # which is wrong because [3] is a valid subarray, and 0 is the "past sum"
        # because between 0 and 3 is 3 no? like from 0-3 is 3 which is our k
        # to combat this, we initialize our dictionary with key 0 : 1(value)
        # this is to handle this edge case of the first number being = k
        # because if 0(as a past sum) already exists, it already has a value of 1!
        # so the final number will be incremented correctly
        # think of the 0 as before the array starts: 0[3,4,2,1] like its "secretely there"
        # between 0 and 3 is 3. so 0 is a "past sum" thats stored before we get to 3(which is the first element)
        # writing these notes down for study puroses later! took an hour but now i understand prefix sums! :D

        pastSums = {0 : 1} # initializing with 0 as discussed above
        current_sum = 0 #the secret 0 as discussed which is the "past sum"
        final = 0 # this variable will store the amount of subarrays formed that = k!

        for num in nums:
            current_sum += num #24
            past_sum = current_sum - k #20
            # now we check, is there a sum weve seen before that if we add
            # it to our current sum will be = k?

            if past_sum in pastSums:
                final += pastSums[past_sum]
            
            if current_sum not in pastSums:
                pastSums[current_sum] = 1
            else:
                pastSums[current_sum] += 1

        return final
                
        