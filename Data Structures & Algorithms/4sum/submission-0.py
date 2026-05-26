class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] ==nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j-1] == nums[j]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        final.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1  
        return final

                        
        