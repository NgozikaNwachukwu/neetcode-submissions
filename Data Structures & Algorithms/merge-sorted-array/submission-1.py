class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # the whole idea about this problem is, we are going to merge the arrays i reverse order
        # since m is the length of the valid numbers in the nums1 array,
        # we are going to use m as a pointer (starting from m - 1) 
        # cuz eg if we have an array [1,2,0,0] m is 2 because they are 2 valid numbers
        # but since m is 2, index 2 is the third element(0) but we are starting the 
        # comparisons from m - 1(2)
        # n is the length of nums2 array. if for example nums2 = [1,2] n = 2 
        # cuz n is the length of the nums 2 array. but in this example, index 2 doesnt exist
        # it ends at index 1. so we start our comparisons from n-1 so we stay in bounds.
        # then we are going to make a pointer at then end of the nums1 array
        # since m is the number of valid numbers in the nums1 array, the only way we can
        #know the last index of the nums1 array is to do m + n - 1. using the examples above,
        # 2+2-1= 3 and as you can see above in our example nums1 array, index 3 is the last element(the last 0)
        # so that is where we will set the last pointer
        # if m-1 is greater than n-1, we will put m-1 in the last position, and decrement m and last
        # if n is greater than or = m, we put n in the last postion and decrement n and l until n has gone past the bunds of nums2 array
        # basically until n becomes less than 0
        # a very important edge case is if we get to the first element in nums1(m = index 0)
        # and the first elemnt in m is greater than the nth element we are comparing it to
        # it will take the last position and there will be no more elements left to compare it to the nth number
        # because we decrement m, so when m becomes -1, its out of bounds. what will happen to that nth number that hasn been compared? and put in nums1?
        # since the nums1 and nums2 lists are sorted in ascending order we can just take the remaining memebers of the nums2 array
        #the ones in the nth positions we are on and keep adding it to the last position and decrementing the last pointer
        # this problem is incredibly difficult jeez. its so hard

        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
                last -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
                last -= 1   
        
        #if after we have done this and we have reached our edge case
        # that n is still greater than or = 0 (uncompared) values
        while n > 0:
            nums1[last] =nums2[n-1]
            n -= 1
            last -= 1

            #another way
            #nums1[m:] = nums2[:n]
        #nums1.sort()
        #Copy all n elements from nums2 into nums1 starting at index m.
        #Sort nums1 in place.
        


    

        