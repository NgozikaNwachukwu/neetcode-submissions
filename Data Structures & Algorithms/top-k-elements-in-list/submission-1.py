class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first step is to create a dictionarry that increments that particular numbers count
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        #next step make the bucket for bucket sort
        bucket = [] # make an aray called bucket, and this bucket will have other empty lists inside(so its a bucket of buckets)
        for _ in range(len(nums) + 1): 
            # we do +1 because each "empty list" we are adding into the bucket has an index(starting from 0)
            #each index represents the count(frequency) of a particular number
            # e.g [10,10,10] the count for 10:3, so we need to put 10 in bucket 3
            # but if we do range(len(nums)) it creates 3 empty lists with indexes: 0, 1 and 2
            # there is no bucket 3 to put 10 in so itll throw an error
            #so we need the length + 1
            bucket.append([])
        # now we have a list : [[], [], [], []] for example
        for i, count in my_dict.items(): #iterate through the whole dictionary
            bucket[count].append(i) # e.g (from the example above) bucket 3 had 10 in it!

        result = []
        for i in range(len(bucket)-1, -1 , -1): # start, stop, step so we are starting at the end and moving backwards by 1
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result 
        