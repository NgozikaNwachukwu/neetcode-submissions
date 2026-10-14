class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arranged = set(nums)
        longest = 0
        for num in arranged: # we are looping over the arranged form of the array
            if num-1 not in arranged: # if the number-1 not in the array it means where are at the beginning of a new consecutive list
                count = 1 # reset the count to 1
                while num+1 in arranged:
                    num += 1 #increment to the next number
                    count += 1 #increment count
                #now we have counted a sequence
                longest = max(count, longest)
        return longest
        # O(2n) due to 2 operations(creation of sets and the loop), but loop runs n times
        # O(n) i used sets. sets is better for space since its O(1) lookup. if i checked 
        # if the array had num-1 it takes O(n) space cuz python has to check the WHOLE array


        