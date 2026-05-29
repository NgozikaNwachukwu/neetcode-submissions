class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stack1 = []
        stack2 = []
        k = k % len(nums)

        for _ in range(k):
            a = nums.pop()
            stack1.append(a)
        #stak1 = [8,7,6,5]
        while len(nums) != 0:
            b = nums.pop()
            stack2.append(b)
        #stack2 = [4, 3, 2, 1]
        #nums is now empty
        while len(stack1) != 0:
            c = stack1.pop()
            nums.append(c)
        
        while len(stack2) != 0:
            d = stack2.pop()
            nums.append(d)
        
        