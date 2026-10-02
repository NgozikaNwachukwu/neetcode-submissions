class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first step is to create a dictionarry that increments that particular numbers count
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        
        output = []
        for _ in range(k):
            vals = list(my_dict.values())
            highest = max(vals)

            for i, num in my_dict.items():
                if num == highest:
                    output.append(i)
                    del my_dict[i]
                    break
        return output
            

        