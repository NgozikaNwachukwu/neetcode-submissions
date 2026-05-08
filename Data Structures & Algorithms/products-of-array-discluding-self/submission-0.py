class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix #multiplication of all the left numbers
            prefix = prefix * nums[i] #expansion of prefix(the multiplying of the numbers on the left for each element of nums and stroing it in the new answers array)
        
        suffix = 1
        for j in range(n-1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
        return answer
        