class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        answer = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1 #this counts the frequencies of each key

        for _ in range(k):
            highest = max(freq, key = freq.get) #means the key w highest frequency
            answer.append(highest)
            del freq[highest] #deleting the number from the dictionary to avoid repetition

        return answer
