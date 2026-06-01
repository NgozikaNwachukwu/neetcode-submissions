class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = len(nums) // 2
        elements = {}
        for num in nums:
            if num in elements:
                elements[num] += 1
            else:
                elements[num] = 1

        # increments the whole dictionary
        for i, count in elements.items(): # iterating through the whole key-vale pairs in dictionary
            if count > target:
                return i
        