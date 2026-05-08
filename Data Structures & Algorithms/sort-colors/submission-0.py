class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ans = []
        for num in nums:
            if num == 0:
                ans.append(num)
        for num in nums:
            if num == 1:
                ans.append(num)
        for num in nums:
            if num ==2:
                ans.append(num)

        nums[:] = ans # trick in python that says take all the contents in 
        #nums array and replace it with what is currently in ans
        #e.g if ans [1,2,3] and nums = [3,2,1] if we do nums[:] = ans
        # nums is now = [1,2,3]
        return nums
            

        