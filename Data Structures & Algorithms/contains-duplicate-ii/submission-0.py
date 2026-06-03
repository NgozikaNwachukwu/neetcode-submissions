class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
        return False
        #brute force, O(n^2) time O(1) space