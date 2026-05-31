class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n//3
        final = []
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        for i, count in my_dict.items():
            if count > target:
                final.append(i)

        return final

        #O(n) time and space
         

        
        