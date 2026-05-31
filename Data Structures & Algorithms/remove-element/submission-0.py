class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #[0,1,3,0,4,_k, _, _] val = 2
        # the whole idea is that we are moving the numbers that are not = val forward
        #going to do this using a pointer that stsrts at the beginning
        # the second pointer, will copy the value of itself into the position of k
        # if its not = val, so that we can move forward and itll increment

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # copying the number in the ith position into
                # the kth position
                k += 1
        return k

                
        