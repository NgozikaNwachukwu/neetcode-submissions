class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array_sum = sum(nums)
        actual_sum = sum(range(len(nums)+1))# adding 1 cuz range stops BEFORE the stated numer
        number = actual_sum - array_sum

        return number